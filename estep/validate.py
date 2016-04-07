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

import jsonschema
import requests
import six
from . import relationship
from .relationship import AbstractValidator

try:
    from jsonschema._format import is_uri as is_uri_orig
except ImportError:
    def is_uri_orig(instance):
        pass

LOGGER = logging.getLogger('estep')


def url_to_path(url):
    prefix, path = url.split('://software.esciencecenter.nl/')
    if prefix == 'https':
        raise ValueError('For the time being, use http instead of https prefixes for http://software.esciencecenter.nl')

    # remove additional indicator
    path = path.split('#')[0]
    return '_' + path + '.md'

def url_to_collection_name(url):
    path = url.split('://software.esciencecenter.nl/')[1]
    return path.split('/')[0]

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


def log_error(error, prefix=""):
    msg = prefix + error.message
    if error.cause is not None:
        msg += ": " + str(error.cause)
    LOGGER.warning(msg)


class AbstractValidators(AbstractValidator, six.moves.UserList):
    def validate(self, name, instance):
        nr_errors = 0
        for validator in self.data:
            nr_errors += validator.validate(name, instance)
        return nr_errors

    def finalize(self):
        nr_errors = 0
        for validator in self.data:
            nr_errors += validator.finalize()
        return nr_errors

    def missing(self):
        for validator in self.data:
            for missing_tuple in validator.missing():
                yield missing_tuple

class PropertyTypoValidator(AbstractValidator):
    """

    >>> validator = PropertyTypoValidator('programmingLanguage')
    >>> validator.validate('noodles', {'programmingLanguage': ['Python']})
    0
    >>> validator.validate('xtas', {'programmingLanguage': ['python']})
    1
    >>> validator.validate('xenon', {'programmingLanguage': ['Java']})
    0

    """
    def __init__(self, property_name):
        self.name = property_name
        self.seen_values = set()
        self.seen_normalized_values = {}

    def validate(self, name, instance):
        if self.name not in instance.keys():
            return 0

        values = instance[self.name]

        nr_errors = 0
        for value in values:
            normalized_value = value.lower()
            if value not in self.seen_values and normalized_value in self.seen_normalized_values:
                error = 'Typo "{0}", already seen as "{1}"'.format(value, self.seen_normalized_values[normalized_value])
                LOGGER.warning('* Error      : ' + error)
                LOGGER.warning('  On property: ' + self.name)
                nr_errors += 1
            self.seen_values.add(value)
            self.seen_normalized_values[normalized_value] = value

        return nr_errors


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



class Validator(AbstractValidator):
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
        self.crossValidators = AbstractValidators()
        self.crossValidators.append(PropertyTypoValidator('programmingLanguage'))
        self.crossValidators.append(PropertyTypoValidator('technologyTag'))
        # From software
        # TODO disable relationship validator, until problems with it have been resolved
        #self.crossValidators += relationship.get_validators()

    def validate(self, name, instance):
        schema_uri = instance['schema']
        errors = list(self.validators[schema_uri].iter_errors(instance))
        has_errors = len(errors) == 0
        if has_errors:
            LOGGER.info('Document: %s OK', name)
        else:
            warning_msg = 'Document: {0} BAD (schema: {1})'.format(name, schema_uri)
            separator = '-'*len(warning_msg)
            LOGGER.warning(separator)
            LOGGER.warning(warning_msg)
            LOGGER.warning(separator + '\n')
            for error in errors:
                LOGGER.warning('* Error      : ' + error.message)
                if error.cause is not None:
                    LOGGER.warning('  Cause      : ' + str(error.cause))
                LOGGER.warning('  On property: ' + '.'.join(list(error.relative_schema_path)[1:]))
                if len(error.context) > 0:
                    LOGGER.warning('  Reasons    :')
                    for c in error.context:
                        LOGGER.warning('  - Error: ' + c.message)
                        if c.cause is not None:
                            LOGGER.warning('    Cause: ' + str(c.cause))

        nr_errors = len(errors)
        nr_errors += self.crossValidators.validate(name, instance)
        return nr_errors

    def finalize(self):
        return self.crossValidators.finalize()
