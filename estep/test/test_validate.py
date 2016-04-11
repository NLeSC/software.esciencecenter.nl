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

from nose.tools import eq_
from ..utils import ValidationError
from ..validate import PropertyTypoValidator


class TestPropertyTypoValidator(object):
    def setUp(self):
        self.validator = PropertyTypoValidator('programmingLanguage')

    def test_single(self):
        python = {'programmingLanguage': ['Python'], '@id': 'http://software.esciencecenter.nl/software/twiqs.nl'}

        result = self.validator.iter_errors(python)

        expected = []
        eq_(list(result), expected)

    def test_multiple(self):
        python = {'programmingLanguage': ['Python'], '@id': 'http://software.esciencecenter.nl/software/twiqs.nl'}
        self.validator.iter_errors(python)
        java = {'programmingLanguage': ['Java'], '@id': 'http://software.esciencecenter.nl/software/twiqs.nl'}
        result = self.validator.iter_errors(java)

        expected = []
        eq_(list(result), expected)

    def test_lowercase(self):
        python1 = {'programmingLanguage': ['Python'], '@id': 'http://software.esciencecenter.nl/software/twiqs.nl'}
        list(self.validator.iter_errors(python1))
        python2 = {'programmingLanguage': ['python'], '@id': 'http://software.esciencecenter.nl/software/twiqs.nl'}
        result = self.validator.iter_errors(python2)

        expected = [ValidationError('Typo "python", already seen as "Python"',
                                    'http://software.esciencecenter.nl/software/twiqs.nl',
                                    'programmingLanguage')]
        eq_(list(result), expected)
