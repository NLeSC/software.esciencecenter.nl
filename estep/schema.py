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
import yaml

import jsonschema
import requests

from .utils import url_to_path, AbstractValidator

try:
    from jsonschema._format import is_uri as is_uri_orig
except ImportError:
    def is_uri_orig(instance):
        pass

LOGGER = logging.getLogger('estep')


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
            with open(schema_fn) as f:
                store[schema_uri] = json.load(f)
    return store


class SchemaValidator(AbstractValidator):
    def __init__(self, schema_uris, schemadir=None, resolve_local=True, resolve_remote=False,
                 resolve_cache_expire=5):
        store = load_schemas(schema_uris, schemadir)

        if resolve_local and resolve_remote:
            LOGGER.debug("Resolving URLs and locating local references")
        elif resolve_local:
            LOGGER.debug("Locating local references")
        elif resolve_remote:
            LOGGER.debug("Resolving URLs")

        self.resolve_local = resolve_local
        self.resolve_remote = resolve_remote
        self.resolve_cache = {}
        self.resolve_cache_expire = resolve_cache_expire

        if resolve_remote and resolve_cache_expire > 0:
            try:
                with open('.cache/resolve/resolve.yml') as f:
                    urls = yaml.load(f)
            except IOError:
                LOGGER.debug('No resolve cache available (.cache/resolve/resolve.yml)')
            else:
                now = datetime.datetime.now()
                for url, stamp in urls.items():
                    if (now - stamp).days <= resolve_cache_expire:
                        self.resolve_cache[url] = stamp

        # Resolve date-time as dates as well as strings
        if isinstance(jsonschema.compat.str_types, type):
            str_types = [jsonschema.compat.str_types]
        else:
            str_types = list(jsonschema.compat.str_types)
        str_types.append(datetime.date)
        types = {u'string': tuple(str_types)}

        format_checker = jsonschema.draft4_format_checker
        format_checker.checkers['uri'] = (self.url_ref, ValueError)

        self.validators = {}
        for schema_uri in schema_uris:
            schema = store[schema_uri]
            resolver = jsonschema.RefResolver(schema_uri, schema,  store=store)
            self.validators[schema_uri] = jsonschema.validators.Draft4Validator(schema,
                                                                                resolver=resolver,
                                                                                types=types,
                                                                                format_checker=format_checker,
                                                                                )

    def url_ref(self, instance):
        # only consider valid uris
        if not is_uri_orig(instance):
            return False

        # handle local urls
        if self.resolve_local and '://software.esciencecenter.nl/' in instance:
            location = url_to_path(instance)
            # do not look for missing directories.
            if os.path.isdir(os.path.dirname(location)) and not os.path.isfile(location):
                err = "{} not found locally as {}".format(instance, location)
                raise ValueError(err)

        # handle remote urls
        if self.resolve_remote and '://software.esciencecenter.nl/' not in instance:
            self.resolve(instance)

        return True

    def resolve(self, url):
        if url in self.resolve_cache:
            return True

        try:
            result = requests.head(url)
            if result.status_code == 404:
                raise ValueError("Remote URL {0} cannot be resolved: not found.".format(url))
            self.resolve_cache[url] = datetime.datetime.now()
        except IOError as ex:
            raise ValueError("Remote URL {0} cannot be resolved: {1}".format(url, ex))

    def iter_errors(self, instance):
        schema_uri = instance['schema']
        for error in self.validators[schema_uri].iter_errors(instance):
            yield error

    def finalize(self):
        if self.resolve_cache_expire > 0:
            cache_str = yaml.safe_dump(self.resolve_cache, default_flow_style=False)
            try:
                if not os.path.isdir('.cache/resolve'):
                    os.makedirs('.cache/resolve')
                with open('.cache/resolve/resolve.yml', 'w') as f:
                    f.write(cache_str)
                LOGGER.debug('Stored resolve cache (.cache/resolve/resolve.yml)')
            except IOError:
                LOGGER.warning('Cannot write to resolve cache (.cache/resolve/resolve.yml)')

        return []
