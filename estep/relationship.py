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

import six

from .utils import (AbstractValidator, ValidationError, check_internal_url,
                    url_to_schema, parse_url, absolute_url)

LOGGER = logging.getLogger('estep')

relationships = [
    ('http://software.esciencecenter.nl/schema/software', 'usedIn',
     'http://software.esciencecenter.nl/schema/project', 'uses'),
    ('http://software.esciencecenter.nl/schema/software', 'dependency',
     'http://software.esciencecenter.nl/schema/software', 'dependencyOf'),
    # FIXME person:contactPerson is for project only? so below not OK?
    ('http://software.esciencecenter.nl/schema/software', 'contactPerson',
     'http://software.esciencecenter.nl/schema/person', 'contactPersonOf'),
    ('http://software.esciencecenter.nl/schema/software', 'owner',
     'http://software.esciencecenter.nl/schema/person', 'ownerOf'),
    ('http://software.esciencecenter.nl/schema/software', 'owner',
     'http://software.esciencecenter.nl/schema/organization', 'ownerOf'),
    ('http://software.esciencecenter.nl/schema/software', 'user',
     'http://software.esciencecenter.nl/schema/person', 'userOf'),
    ('http://software.esciencecenter.nl/schema/software', 'user',
     'http://software.esciencecenter.nl/schema/organization', 'userOf'),
    ('http://software.esciencecenter.nl/schema/software', 'contributor',
     'http://software.esciencecenter.nl/schema/person', 'contributorOf'),
    ('http://software.esciencecenter.nl/schema/project', 'contactPerson',
     'http://software.esciencecenter.nl/schema/person', 'contactPersonOf'),
    ('http://software.esciencecenter.nl/schema/project', 'coordinator',
     'http://software.esciencecenter.nl/schema/person', 'coordinatorOf'),
    ('http://software.esciencecenter.nl/schema/project', 'engineer',
     'http://software.esciencecenter.nl/schema/person', 'engineerOf'),
    ('http://software.esciencecenter.nl/schema/project', 'principalInvestigator',
     'http://software.esciencecenter.nl/schema/person', 'principalInvestigatorOf'),
    # FIXME software:involvedOrganization has no counterpart in organization schema
    # From project
    ('http://software.esciencecenter.nl/schema/project', 'involvedOrganization',
     'http://software.esciencecenter.nl/schema/organization', 'involvedIn'),
    ('http://software.esciencecenter.nl/schema/report', 'author',
     'http://software.esciencecenter.nl/schema/organization', 'authorOfReport'),
    ('http://software.esciencecenter.nl/schema/report', 'author',
     'http://software.esciencecenter.nl/schema/person', 'authorOfReport'),
    # FIXME project:publication <> publication:author relationship needs checking
    # but project:publication[0] != publication:@id as project:publication[0] == publicatoin:doi
]


def get_validators():
    return [RelationshipValidator(*r) for r in relationships]


def is_relationship_value(value, otherschema):
    if not isinstance(value, str):
        return False
    try:
        url = parse_url(value)
        check_internal_url(url)
        if url_to_schema(url) != otherschema:
            raise ValueError(value)
    except ValueError:
        return False
    else:
        return True


def instance_relationships(instance, schema, property_name, otherschema):
    if instance['schema'] != schema:
        raise TypeError(instance)
    if property_name not in instance:
        raise KeyError(property_name)

    value = instance[property_name]
    if is_relationship_value(value, otherschema):
        return set([absolute_url(value)])
    elif isinstance(value, dict):
        # not a @id
        raise ValueError(value)
    else:
        result = set()
        for entry in value:
            if is_relationship_value(entry, otherschema):
                result.add(absolute_url(entry))
        return result


class RelationshipValidator(AbstractValidator):
    """Bi-directional relationship validator

    Validation is delayed, iter_errors records relationships in instance
    and finalize() checks which relationships are missing
    """
    def __init__(self, schema1, prop1, schema2, prop2):
        self.schema1 = schema1
        self.prop1 = prop1
        self.memory1 = {}
        self.schema2 = schema2
        self.prop2 = prop2
        self.memory2 = {}

    def iter_errors(self, instance):
        myid = instance['@id']

        try:
            if instance['schema'] == self.schema1 and self.prop1 in instance:
                self.memory1[myid] = instance_relationships(
                    instance, self.schema1, self.prop1, self.schema2)
        except Exception as ex:
            yield ex
        try:
            if instance['schema'] == self.schema2 and self.prop2 in instance:
                self.memory2[myid] = instance_relationships(
                    instance, self.schema2, self.prop2, self.schema1)
        except Exception as ex:
            yield ex

    def missing(self):
        for myid, myvalues in six.iteritems(self.memory1):
            for myvalue in myvalues:
                if myvalue in self.memory2 and myid in self.memory2[myvalue]:
                    pass
                else:
                    yield (myvalue, self.prop2, myid)

        for myid, myvalues in six.iteritems(self.memory2):
            for myvalue in myvalues:
                if myvalue in self.memory1 and myid in self.memory1[myvalue]:
                    pass
                else:
                    yield (myvalue, self.prop1, myid)

    def finalize(self):
        for source, property_name, target in self.missing():
            message = 'Missing "{}"'.format(target)
            yield ValidationError(message, source, property_name)

    def __repr__(self):
        return 'RelationshipValidator<{}, {}, {}, {}>'.format(
            self.schema1, self.prop1, self.schema2, self.prop2)
