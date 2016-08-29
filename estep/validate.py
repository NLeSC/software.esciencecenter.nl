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

import logging

from jsonschema.exceptions import ValidationError as SchemaValidationError

from . import relationship
from .schema import SchemaValidator
from .utils import AbstractValidator, ValidationError

LOGGER = logging.getLogger('estep')


def log_error(error):
    if isinstance(error, SchemaValidationError):
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
    else:
        LOGGER.warning(error)


class Validators(AbstractValidator):
    def __init__(self, validators):
        self.validators = validators

    def iter_errors(self, instance):
        for validator in self.validators:
            for error in validator.iter_errors(instance):
                yield error

    def finalize(self):
        for validator in self.validators:
            for error in validator.finalize():
                yield error

    def missing(self):
        for validator in self.validators:
            for missing_tuple in validator.missing():
                yield missing_tuple


class PropertyTypoValidator(AbstractValidator):
    def __init__(self, property_name):
        self.property_name = property_name
        self.seen_values = set()
        self.seen_normalized_values = {}

    def iter_errors(self, instance):
        if self.property_name not in instance:
            return

        values = instance[self.property_name]

        for value in values:
            normalized_value = value.lower()
            if value not in self.seen_values and normalized_value in self.seen_normalized_values:
                message = 'Typo "{0}", already seen as "{1}"'.format(value, self.seen_normalized_values[normalized_value])
                yield ValidationError(message, instance['@id'], self.property_name)
            self.seen_values.add(value)
            self.seen_normalized_values[normalized_value] = value


class EStepValidator(Validators):
    def __init__(self, schema_uris, schemadir=None, resolve_local=True, resolve_remote=False,
                 resolve_cache_expire=5):
        validators = [
            SchemaValidator(schema_uris, schemadir, resolve_local,
                            resolve_remote,
                            resolve_cache_expire=resolve_cache_expire),
            PropertyTypoValidator('programmingLanguage'),
            PropertyTypoValidator('technologyTag'),
        ]
        validators += relationship.get_validators()
        super(EStepValidator, self).__init__(validators)
