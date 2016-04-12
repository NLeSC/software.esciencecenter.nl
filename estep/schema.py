# Copyright 2016 Netherlands eScience Center
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
import json
import os
import logging
import codecs

import jsonschema
import requests

from .utils import url_to_path, AbstractValidator

try:
    from jsonschema._format import is_uri as is_uri_orig
except ImportError:
    def is_uri_orig(instance):
        pass

LOGGER = logging.getLogger('estep')


def url_ref(instance):
    return url_local_ref(instance) and url_resolve(instance)


def url_local_ref(instance):
    if not is_uri_orig(instance):
        return False

    # lookup local files locally
    if '://software.esciencecenter.nl/' in instance:
        location = url_to_path(instance)
        # do not look for missing directories.
        if os.path.isdir(os.path.dirname(location)) and not os.path.isfile(location):
            err = "{} not found locally as {}".format(instance, location)
            raise ValueError(err)

    return True


def url_resolve(instance):
    if not is_uri_orig(instance):
        return False

    # do not resolve URLs of current code
    if '://software.esciencecenter.nl/' in instance:
        return True

    try:
        result = requests.head(instance)
        if result.status_code == 404:
            raise ValueError("Remote URL {0} cannot be resolved: not found.".format(instance))
    except IOError as ex:
        raise ValueError("Remote URL {0} cannot be resolved: {1}".format(instance, ex))

    return True


def load_schemas(schema_uris, schemadir=None):
    store = {}
    for schema_uri in schema_uris:
        if schemadir is None:
            u = schema_uri
            request = requests.get(u)
            # do not accept failed calls
            try:
                request.raise_for_status()
            except requests.exceptions.HTTPError as ex:
                LOGGER.error("cannot load schema %s:\n\t%s\nUse --local to load local schemas.", schema_uri, ex)

            store[schema_uri] = request.json()
        else:
            LOGGER.debug('Loading schema %s from %s', schema_uri, schemadir)
            schema_fn = schema_uri.replace('http://software.esciencecenter.nl/schema', schemadir)
            with codecs.open(schema_fn, encoding='utf-8') as f:
                store[schema_uri] = json.load(f)
    return store


class SchemaValidator(AbstractValidator):
    def __init__(self, schema_uris, schemadir=None, resolve_local=True, resolve_remote=False):
        store = load_schemas(schema_uris, schemadir)

        # Resolve date-time as dates as well as strings
        if isinstance(jsonschema.compat.str_types, type):
            str_types = [jsonschema.compat.str_types]
        else:
            str_types = list(jsonschema.compat.str_types)
        str_types.append(datetime.date)
        types = {u'string': tuple(str_types)}

        format_checker = jsonschema.draft4_format_checker
        if resolve_local and resolve_remote:
            LOGGER.debug("Resolving URLs and locating local references")
            format_checker.checkers['uri'] = (url_ref, ValueError)
        elif resolve_local:
            LOGGER.debug("Locating local references")
            format_checker.checkers['uri'] = (url_local_ref, ValueError)
        elif resolve_remote:
            LOGGER.debug("Resolving URLs")
            format_checker.checkers['uri'] = (url_resolve, ValueError)

        self.validators = {}
        for schema_uri in schema_uris:
            schema = store[schema_uri]
            resolver = jsonschema.RefResolver(schema_uri, schema,  store=store)
            self.validators[schema_uri] = jsonschema.validators.Draft4Validator(schema,
                                                                                resolver=resolver,
                                                                                types=types,
                                                                                format_checker=format_checker,
                                                                                )

    def iter_errors(self, instance):
        schema_uri = instance['schema']
        for error in self.validators[schema_uri].iter_errors(instance):
            yield error
