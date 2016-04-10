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


class AbstractValidator(object):
    def validate(self, instance):
        for error in self.iter_errors(instance):
            raise error

    def finalize(self):
        return []

    def iter_errors(self, instance):
        raise NotImplementedError


class ValidationError(ValueError):
    def __init__(self, message, document_name, property_name):
        super(ValidationError, self).__init__(message)
        self.message = message
        self.document_name = document_name
        self.property_name = property_name

    def __str__(self):
        return '{}:{}: {}'.format(url_to_path(self.document_name), self.property_name, self.message)

    def __repr__(self):
        return "ValidationError('{}', '{}', '{}')".format(self.message, self.document_name, self.property_name)

    def __eq__(self, other):
        return self.message == other.message and self.document_name == other.document_name and self.property_name == other.property_name


def check_internal_url(url):
    if '://software.esciencecenter.nl/' not in url:
        raise ValueError('Url {} is not internal'.format(url))


def url_to_path(url):
    check_internal_url(url)
    prefix, path = url.split('://software.esciencecenter.nl/')
    if prefix == 'https':
        raise ValueError('For the time being, use http instead of https prefixes for http://software.esciencecenter.nl')

    # remove additional indicator
    path = path.split('#')[0]
    return '_' + path + '.md'


def url_to_schema(url):
    check_internal_url(url)
    return 'http://software.esciencecenter.nl/schema/' + url_to_collection_name(url)


def url_to_collection_name(url):
    path = url.split('://software.esciencecenter.nl/')[1]
    return path.split('/')[0]
