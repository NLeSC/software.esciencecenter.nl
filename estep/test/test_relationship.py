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

from ..relationship import RelationshipValidator
from ..utils import ValidationError
from ..validate import Validators
from nose.tools import eq_


class TestArrayRelationshipValidator(object):
    def setUp(self):
        self.validator = RelationshipValidator('http://software.esciencecenter.nl/schema/software',
                                               'usedIn',
                                               'http://software.esciencecenter.nl/schema/project',
                                               'uses')

    def test_relationship_bidirectional(self):
        twinl = {'schema': 'http://software.esciencecenter.nl/schema/project',
                 '@id': 'http://software.esciencecenter.nl/project/twinl',
                 'uses': ['http://software.esciencecenter.nl/software/twiqs.nl']}
        self.validator.validate(twinl)
        twiqsnl = {'schema': 'http://software.esciencecenter.nl/schema/software',
                   '@id': 'http://software.esciencecenter.nl/software/twiqs.nl',
                   'usedIn': ['http://software.esciencecenter.nl/project/twinl']}
        self.validator.validate(twiqsnl)

        eq_(list(self.validator.finalize()), [])

    def test_relationship_leftmissing(self):
        twinl = {'schema': 'http://software.esciencecenter.nl/schema/project',
                 '@id': 'http://software.esciencecenter.nl/project/twinl',
                 'uses': []}
        self.validator.validate(twinl)
        twiqsnl = {'schema': 'http://software.esciencecenter.nl/schema/software',
                   '@id': 'http://software.esciencecenter.nl/software/twiqs.nl',
                   'usedIn': ['http://software.esciencecenter.nl/project/twinl']}
        self.validator.validate(twiqsnl)

        result = list(self.validator.finalize())

        expected = [ValidationError('Missing "http://software.esciencecenter.nl/software/twiqs.nl"',
                                    'http://software.esciencecenter.nl/project/twinl',
                                    'uses')]
        eq_(result, expected)

    def test_relationship_rightmissing(self):
        twinl = {'schema': 'http://software.esciencecenter.nl/schema/project',
                 '@id': 'http://software.esciencecenter.nl/project/twinl',
                 'uses': ['http://software.esciencecenter.nl/software/twiqs.nl']}
        self.validator.validate(twinl)
        twiqsnl = {'schema': 'http://software.esciencecenter.nl/schema/software',
                   '@id': 'http://software.esciencecenter.nl/software/twiqs.nl',
                   'usedIn': []}
        self.validator.validate(twiqsnl)

        expected = [ValidationError('Missing "http://software.esciencecenter.nl/project/twinl"',
                                    'http://software.esciencecenter.nl/software/twiqs.nl',
                                    'usedIn')]
        eq_(list(self.validator.finalize()), expected)


class TestScalarRelationshipValidator(object):
    def setUp(self):
        self.validator = RelationshipValidator('http://software.esciencecenter.nl/schema/software',
                                               'contactPerson',
                                               'http://software.esciencecenter.nl/schema/person',
                                               'contactPersonOf')

    def test_relationship_bidirectional(self):
        erik = {'schema': 'http://software.esciencecenter.nl/schema/person',
                '@id': 'http://software.esciencecenter.nl/person/e.tjongkimsang',
                'contactPersonOf': ['http://software.esciencecenter.nl/software/twiqs.nl']}

        self.validator.validate(erik)
        twiqsnl = {'schema': 'http://software.esciencecenter.nl/schema/software',
                   '@id': 'http://software.esciencecenter.nl/software/twiqs.nl',
                   'contactPerson': 'http://software.esciencecenter.nl/person/e.tjongkimsang'}
        self.validator.validate(twiqsnl)

        eq_(list(self.validator.finalize()), [])

    def test_relationship_contactPersonmissing(self):
        erik = {'schema': 'http://software.esciencecenter.nl/schema/person',
                '@id': 'http://software.esciencecenter.nl/person/e.tjongkimsang',
                }

        self.validator.validate(erik)
        twiqsnl = {'schema': 'http://software.esciencecenter.nl/schema/software',
                   '@id': 'http://software.esciencecenter.nl/software/twiqs.nl',
                   'contactPerson': 'http://software.esciencecenter.nl/person/e.tjongkimsang'}
        self.validator.validate(twiqsnl)

        result = list(self.validator.finalize())

        expected = [ValidationError('Missing "http://software.esciencecenter.nl/software/twiqs.nl"',
                                    'http://software.esciencecenter.nl/person/e.tjongkimsang',
                                    'contactPersonOf')]
        eq_(result, expected)

    def test_relationship_contactPersonOftmissing(self):
        erik = {'schema': 'http://software.esciencecenter.nl/schema/person',
                '@id': 'http://software.esciencecenter.nl/person/e.tjongkimsang',
                'contactPersonOf': ['http://software.esciencecenter.nl/software/twiqs.nl']}

        self.validator.validate(erik)
        twiqsnl = {'schema': 'http://software.esciencecenter.nl/schema/software',
                   '@id': 'http://software.esciencecenter.nl/software/twiqs.nl',
                   }
        self.validator.validate(twiqsnl)

        expected = [ValidationError('Missing "http://software.esciencecenter.nl/person/e.tjongkimsang"',
                                    'http://software.esciencecenter.nl/software/twiqs.nl',
                                    'contactPerson')]
        eq_(list(self.validator.finalize()), expected)


class Test1to2RelationshipValidators(object):
    def setUp(self):
        personOwner = RelationshipValidator('http://software.esciencecenter.nl/schema/software',
                                            'owner',
                                            'http://software.esciencecenter.nl/schema/person',
                                            'ownerOf')
        organizationOwner = RelationshipValidator('http://software.esciencecenter.nl/schema/software',
                                                  'owner',
                                                  'http://software.esciencecenter.nl/schema/organization',
                                                  'ownerOf')
        self.validator = Validators([personOwner, organizationOwner])

    def test_personOwns(self):
        erik = {'schema': 'http://software.esciencecenter.nl/schema/person',
                '@id': 'http://software.esciencecenter.nl/person/e.tjongkimsang',
                'ownerOf': ['http://software.esciencecenter.nl/software/twiqs.nl']}
        self.validator.validate(erik)

        twiqsnl = {'schema': 'http://software.esciencecenter.nl/schema/software',
                   '@id': 'http://software.esciencecenter.nl/software/twiqs.nl',
                   'owner': ['http://software.esciencecenter.nl/person/e.tjongkimsang']}
        self.validator.validate(twiqsnl)
        nlesc = {'schema': 'http://software.esciencecenter.nl/schema/organization',
                 '@id': 'http://software.esciencecenter.nl/organization/nlesc',
                 'ownerOf': []}
        self.validator.validate(nlesc)

        result = self.validator.finalize()
        eq_(list(result), [])

    def test_personOwns_missingowner(self):
        erik = {'schema': 'http://software.esciencecenter.nl/schema/person',
                '@id': 'http://software.esciencecenter.nl/person/e.tjongkimsang',
                'ownerOf': ['http://software.esciencecenter.nl/software/twiqs.nl']}
        self.validator.validate(erik)

        twiqsnl = {'schema': 'http://software.esciencecenter.nl/schema/software',
                   '@id': 'http://software.esciencecenter.nl/software/twiqs.nl',
                   'owner': []}
        self.validator.validate(twiqsnl)
        nlesc = {'schema': 'http://software.esciencecenter.nl/schema/organization',
                 '@id': 'http://software.esciencecenter.nl/organization/nlesc',
                 'ownerOf': []}
        self.validator.validate(nlesc)

        result = self.validator.finalize()

        expected = [ValidationError('Missing "http://software.esciencecenter.nl/person/e.tjongkimsang"',
                                    'http://software.esciencecenter.nl/software/twiqs.nl',
                                    'owner')]
        eq_(list(result), expected)

    def test_personOwns_missingpersonownerof(self):
        erik = {'schema': 'http://software.esciencecenter.nl/schema/person',
                '@id': 'http://software.esciencecenter.nl/person/e.tjongkimsang',
                'ownerOf': []}
        self.validator.validate(erik)

        twiqsnl = {'schema': 'http://software.esciencecenter.nl/schema/software',
                   '@id': 'http://software.esciencecenter.nl/software/twiqs.nl',
                   'owner': ['http://software.esciencecenter.nl/person/e.tjongkimsang']}
        self.validator.validate(twiqsnl)
        nlesc = {'schema': 'http://software.esciencecenter.nl/schema/organization',
                 '@id': 'http://software.esciencecenter.nl/organization/nlesc',
                 'ownerOf': []}
        self.validator.validate(nlesc)

        result = self.validator.finalize()
        expected = [ValidationError('Missing "http://software.esciencecenter.nl/software/twiqs.nl"',
                                    'http://software.esciencecenter.nl/person/e.tjongkimsang',
                                    'ownerOf')]
        eq_(list(result), expected)

    def test_personOwns_andownerOfOtherSchema(self):
        erik = {'schema': 'http://software.esciencecenter.nl/schema/person',
                '@id': 'http://software.esciencecenter.nl/person/e.tjongkimsang',
                'ownerOf': ['http://software.esciencecenter.nl/software/twiqs.nl', 'http://software.esciencecenter.nl/project/twinl']}
        self.validator.validate(erik)

        twiqsnl = {'schema': 'http://software.esciencecenter.nl/schema/software',
                   '@id': 'http://software.esciencecenter.nl/software/twiqs.nl',
                   'owner': ['http://software.esciencecenter.nl/person/e.tjongkimsang']}
        self.validator.validate(twiqsnl)
        nlesc = {'schema': 'http://software.esciencecenter.nl/schema/organization',
                 '@id': 'http://software.esciencecenter.nl/organization/nlesc',
                 'ownerOf': []}
        self.validator.validate(nlesc)

        result = self.validator.finalize()
        expected = []
        eq_(list(result), expected)
