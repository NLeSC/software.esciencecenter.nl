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
import logging
import jsonschema
import requests


LOGGER = logging.getLogger('estep')


class Validator(object):
    def __init__(self, schema_uris, schemadir=None):
        store = {}
        for schema_uri in schema_uris:
            if schemadir is None:
                u = schema_uri
                # TODO remove replace when domains are fixed
                u = u.replace('estep.esciencecenter.nl', 'estep.github.io')
                request = requests.get(u)
                # do not accept failed calls
                try:
                    request.raise_for_status()
                except requests.exceptions.HTTPError as ex:
                    LOGGER.error("cannot load schema %s:\n\t%s\nUse --schemadir=schema to load local schemas.", schema_uri, ex)

                store[schema_uri] = request.json()
            else:
                LOGGER.debug('Loading schema %s from %s', schema_uri, schemadir)
                schema_fn = schema_uri.replace('http://estep.esciencecenter.nl/schema', schemadir)
                with open(schema_fn) as f:
                    store[schema_uri] = json.load(f)

        # Resolve date-time as dates as well as strings
        if isinstance(jsonschema.compat.str_types, type):
            str_types = [jsonschema.compat.str_types]
        else:
            str_types = list(jsonschema.compat.str_types)
        str_types.append(datetime.date)
        types = {u'string': tuple(str_types)}

        self.validators = {}
        for schema_uri in schema_uris:
            schema = store[schema_uri]
            resolver = jsonschema.RefResolver(schema_uri, schema,  store=store)
            self.validators[schema_uri] = jsonschema.Draft4Validator(schema, resolver=resolver, types=types)

    def validate(self, name, instance):
        schema_uri = instance['schema']
        errors = list(self.validators[schema_uri].iter_errors(instance))
        has_errors = len(errors) == 0
        if has_errors:
            LOGGER.info('Document: %s OK', name)
        else:
            LOGGER.warning('Document: %s BAD (schema:%s)\n-------------------------------------------------\n', name, schema_uri)
            for error in errors:
                LOGGER.warning(error)
            LOGGER.warning('-------------------------------------------------')
        return len(errors)
