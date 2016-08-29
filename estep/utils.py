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
import requests
from requests.packages.urllib3 import Retry

import rfc3987
import requests
import mimetypes
import os


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
        return '{}:{}: {}'.format(
            url_to_path(parse_url(self.document_name)), self.property_name,
            self.message)

    def __repr__(self):
        return "ValidationError('{}', '{}', '{}')".format(
            self.message, self.document_name, self.property_name)

    def __eq__(self, other):
        return (self.message == other.message and
                self.document_name == other.document_name and
                self.property_name == other.property_name)


def check_internal_url(url):
    if not is_internal_url(url):
        raise ValueError('Url {} is not internal'
                         .format(rfc3987.compose(**url)))


def is_internal_url(url):
    is_internal = url['authority'] in (None, 'software.esciencecenter.nl')
    if is_internal and not url['path'].startswith('/'):
        raise ValueError('Path {} must start with /'
                         .format(rfc3987.compose(**url)))

    if is_internal and url['scheme'] == 'https':
        raise ValueError('For the time being, use http instead of https '
                         'prefixes for http://software.esciencecenter.nl')
    return is_internal


def absolute_url(url):
    url = parse_url(url)
    if url['authority'] is None:
        url['scheme'] = 'http'
        url['authority'] = 'software.esciencecenter.nl'
    return rfc3987.compose(**url)


def url_to_path(url):
    check_internal_url(url)
    return '_' + url['path'].lstrip('/') + '.md'


def url_to_schema(url):
    check_internal_url(url)
    return ('http://software.esciencecenter.nl/schema/' +
            url_to_collection_name(url))


def url_to_collection_name(url):
    return url['path'].split('/')[1]


def parse_url(url):
    return rfc3987.parse(url)


def download_file(url, base_path):
    r = requests.get(url)
    r.raise_for_status()
    ext = os.path.splitext(url)[1]
    if len(ext) == 0:
        if 'content-type' in r.headers:
            ext = mimetypes.guess_extension(
                r.headers['content-type'].split(';')[0])
        else:
            raise ValueError("Cannot determine file type of {}".format(url))

    path = base_path + ext
    with open(path, 'wb') as f:
        f.write(r.content)

    return path


def retrying_http_session(retries=3):
    """Returns a requests session with performs retries on dns, connection, read errors.

    Also retries when server returns 500 error code.

    Args:
        retries (int): Number of retries for a request

    Returns:
        requests.Session()
    """
    http_session = requests.Session()
    http_adapter = requests.adapters.HTTPAdapter()
    retry = Retry(total=retries, status_forcelist=[500])
    http_adapter.max_retries = retry
    http_session.mount('http://', http_adapter)
    http_session.mount('https://', http_adapter)
    return http_session
