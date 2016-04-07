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

import collections

import jsonschema
import requests
import six

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
        prefix, path = instance.split('://software.esciencecenter.nl/')
        if prefix == 'https':
            raise ValueError('For the time being, use http instead of https prefixes for http://software.esciencecenter.nl')

        # remove additional indicator
        path = path.split('#')[0]
        location = '_' + path + '.md'
        # do not look for missing directories.
        if os.path.isdir(os.path.dirname(location)) and not os.path.isfile(location):
            err = "{} not found locally as {}".format(instance, location)
            raise ValueError(err)

    return True


def url_resolve(instance):
    if not is_uri_orig(instance):
        return False

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


class AbstractValidator(object):
    def validate(self, name, instance):
        # TODO yield errors instead of logging errors and returning nr_errors
        raise NotImplementedError

    def finalize(self):
        # TODO yield errors instead of logging errors and returning nr_errors
        return 0


class AbstractValidators(AbstractValidator, collections.UserList):
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


class RelationShipValidator(AbstractValidator):
    """

    >>> validator = RelationShipValidator('http://software.esciencecenter.nl/schema/software', 'usedIn',
    ...                                   'http://software.esciencecenter.nl/schema/project', 'uses')
    >>> validator.validate('twinl', {'schema': 'http://software.esciencecenter.nl/schema/project',
    ...                              '@id': 'http://software.esciencecenter.nl/project/twinl',
    ...                              'uses': ['http://software.esciencecenter.nl/software/twiqs.nl']})
    ... # twinl uses twiqs.nl, but twiqs.nl has not been seen yet, so OK for now
    0
    >>> validator.validate('twiqs.nl', {'schema': 'http://software.esciencecenter.nl/schema/software',
    ...                                 '@id': 'http://software.esciencecenter.nl/software/twiqs.nl',
    ...                                 'usedIn': ['http://software.esciencecenter.nl/project/twinl']})
    ... # twiqs.nl is used in twinl and twinl uses twiqs.nl, so is OK
    0
    >>> validator.validate('emetabolomics', {'schema': 'http://software.esciencecenter.nl/schema/project',
    ...                                      '@id': 'http://software.esciencecenter.nl/project/emetabolomics',
    ...                                      'uses': ['http://software.esciencecenter.nl/software/xenon']})
    ... # xenon is used by emetabolomics, but xenon has not been seen yet, so OK for now
    0
    >>> validator.validate('xenon', {'schema': 'http://software.esciencecenter.nl/schema/software',
    ...                              '@id': 'http://software.esciencecenter.nl/software/xenon',
    ...                              'usedIn': ['http://software.esciencecenter.nl/project/simcity']})
    ... # xenon is used by emetabolomics, but xenon is not used in emetabolomics, so gives error
    1
    >>> validator.validate('simcity', {'schema': 'http://software.esciencecenter.nl/schema/project',
    ...                                '@id': 'http://software.esciencecenter.nl/project/simcity',
    ...                                'uses': ['http://software.esciencecenter.nl/software/pyxenon']})
    ... # xenon is used in simcity, but simcity does not use xenon, so gives error
    1
    >>> validator.finalize()
    ... # simcity uses pyxenon, but validator has not seen pyxenon, so gives error
    1

    """
    def __init__(self, schema1, prop1, schema2, prop2):
        self.schema1 = schema1
        self.prop1 = prop1
        self.memory1 = {}
        self.schema2 = schema2
        self.prop2 = prop2
        self.memory2 = {}
        self.errors = set()

    def validate(self, name, instance):
        schema = instance['schema']
        myid = instance['@id']
        nr_errors = 0

        if schema == self.schema1 and self.prop1 in instance:
            if isinstance(instance[self.prop1], str):
                myvalues = set([instance[self.prop1]])
            elif isinstance(instance[self.prop1], dict):
                # not a @id
                return nr_errors
            else:
                myvalues = set([d for d in instance[self.prop1] if isinstance(d, str)])

            for myvalue in myvalues:
                if myvalue not in self.memory2:
                    LOGGER.debug('Unable to validate {0} {1} {2}, have not seen counterpart yet'.format(myid, self.prop1, myvalue))
                    continue
                if myid in self.memory2[myvalue]:
                    LOGGER.debug('{0} {1} {2} and {2} {3} {0}'.format(myid, self.prop1, myvalue, self.prop2))
                    continue
                error = 'Missing "{0}"'.format(myid)
                LOGGER.warning('* Error      : ' + error)
                LOGGER.warning('  On property: ' + self.prop2 + ' of ' + myvalue)
                self.errors.add((myid, self.prop2, myvalue))
                nr_errors += 1

            # find other direction
            for otherid, othervalues in six.iteritems(self.memory2):
                if myid in othervalues and otherid not in myvalues:
                    error = 'Missing "{0}"'.format(otherid)
                    LOGGER.warning('* Error      : ' + error)
                    LOGGER.warning('  On property: ' + self.prop1)
                    self.errors.add((otherid, self.prop1, myid))
                    nr_errors += 1

            self.memory1[myid] = myvalues
        if schema == self.schema2 and self.prop2 in instance:
            if isinstance(instance[self.prop2], str):
                myvalues = set([instance[self.prop2]])
            elif isinstance(instance[self.prop2], dict):
                # not a @id
                return nr_errors
            else:
                myvalues = set([d for d in instance[self.prop2] if isinstance(d, str)])

            for myvalue in myvalues:
                if myvalue not in self.memory1:
                    LOGGER.debug('Unable to validate {0} {1} {2}, have not seen counterpart yet'.format(myid, self.prop2, myvalue))
                    continue
                if myid in self.memory1[myvalue]:
                    LOGGER.debug('{0} {1} {2} and {2} {3} {0}'.format(myid, self.prop2, myvalue, self.prop1))
                    continue
                error = 'Missing "{0}"'.format(myid)
                LOGGER.warning('* Error      : ' + error)
                LOGGER.warning('  On property: ' + self.prop1 + ' of ' + myvalue)
                self.errors.add((myid, self.prop1, myvalue))
                nr_errors += 1

            # find other direction
            for otherid, othervalues in six.iteritems(self.memory1):
                if myid in othervalues and otherid not in myvalues:
                    error = 'Missing "{0}"'.format(otherid)
                    LOGGER.warning('* Error      : ' + error)
                    LOGGER.warning('  On property: ' + self.prop2)
                    self.errors.add((otherid, self.prop2, myid))
                    nr_errors += 1

            self.memory2[myid] = myvalues

        return nr_errors

    def finalize(self):
        nr_errors = 0
        for myid, myvalues in six.iteritems(self.memory1):
            for myvalue in myvalues:
                if myvalue in self.memory2 and myid in self.memory2[myvalue]:
                    pass
                else:
                    error = 'Missing "{0}"'.format(myid)
                    if (myid, self.prop2, myvalue) not in self.errors:
                        LOGGER.warning('* Error      : ' + error)
                        LOGGER.warning('  On property: ' + self.prop2 + ' of ' + myvalue)
                        nr_errors += 1

        for myid, myvalues in six.iteritems(self.memory2):
            for myvalue in myvalues:
                if myvalue in self.memory1 and myid in self.memory1[myvalue]:
                    pass
                else:
                    # error = '"{0}" not found locally'.format(myvalue)
                    error = 'Missing "{0}"'.format(myid)
                    if (myid, self.prop1, myvalue) not in self.errors:
                        LOGGER.warning('* Error      : ' + error)
                        LOGGER.warning('  On property: ' + self.prop1 + ' of ' + myvalue)
                        nr_errors += 1

        return nr_errors


class Validator(AbstractValidator):
    def __init__(self, schema_uris, schemadir=None, resolve_local=True, resolve_remote=False):
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
        self.crossValidators.append(RelationShipValidator('http://software.esciencecenter.nl/schema/software',
                                                          'usedIn',
                                                          'http://software.esciencecenter.nl/schema/project',
                                                          'uses'))
        self.crossValidators.append(RelationShipValidator('http://software.esciencecenter.nl/schema/software',
                                                          'dependency',
                                                          'http://software.esciencecenter.nl/schema/software',
                                                          'dependencyOf'))
        # FIXME person:contactPerson is for project only? so below not OK?
        self.crossValidators.append(RelationShipValidator('http://software.esciencecenter.nl/schema/software',
                                                          'contactPerson',
                                                          'http://software.esciencecenter.nl/schema/person',
                                                          'contactPersonOf'))
        self.crossValidators.append(RelationShipValidator('http://software.esciencecenter.nl/schema/software',
                                                          'owner',
                                                          'http://software.esciencecenter.nl/schema/person',
                                                          'ownerOf'))
        self.crossValidators.append(RelationShipValidator('http://software.esciencecenter.nl/schema/software',
                                                          'owner',
                                                          'http://software.esciencecenter.nl/schema/organization',
                                                          'ownerOf'))
        self.crossValidators.append(RelationShipValidator('http://software.esciencecenter.nl/schema/software',
                                                          'user',
                                                          'http://software.esciencecenter.nl/schema/person',
                                                          'userOf'))
        self.crossValidators.append(RelationShipValidator('http://software.esciencecenter.nl/schema/software',
                                                          'user',
                                                          'http://software.esciencecenter.nl/schema/organization',
                                                          'userOf'))
        self.crossValidators.append(RelationShipValidator('http://software.esciencecenter.nl/schema/software',
                                                          'contributor',
                                                          'http://software.esciencecenter.nl/schema/person',
                                                          'contributorOf'))
        # FIXME software:involvedOrganization has no counterpart in organization schema
        # From project
        self.crossValidators.append(RelationShipValidator('http://software.esciencecenter.nl/schema/project',
                                                          'contactPerson',
                                                          'http://software.esciencecenter.nl/schema/person',
                                                          'contactPersonOf'))
        self.crossValidators.append(RelationShipValidator('http://software.esciencecenter.nl/schema/project',
                                                          'coordinator',
                                                          'http://software.esciencecenter.nl/schema/person',
                                                          'coordinatorOf'))
        self.crossValidators.append(RelationShipValidator('http://software.esciencecenter.nl/schema/project',
                                                          'engineer',
                                                          'http://software.esciencecenter.nl/schema/person',
                                                          'engineerOf'))
        self.crossValidators.append(RelationShipValidator('http://software.esciencecenter.nl/schema/project',
                                                          'principalInvestigator',
                                                          'http://software.esciencecenter.nl/schema/person',
                                                          'principalInvestigatorOf'))
        self.crossValidators.append(RelationShipValidator('http://software.esciencecenter.nl/schema/project',
                                                          'involvedOrganization',
                                                          'http://software.esciencecenter.nl/schema/organization',
                                                          'involvedIn'))
        # FIXME person:affiliation has no counterpart in organization schema

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
