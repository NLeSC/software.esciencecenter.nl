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

from __future__ import print_function
from datetime import datetime
from os.path import isfile
import logging
from six.moves.urllib.parse import urlparse

from .format import object2jekyll
from .utils import retrying_http_session

LOGGER = logging.getLogger('estep')


def fetch_csljson(doi):
    headers = {'Accept': 'application/vnd.citationstyles.csl+json'}
    http_session = retrying_http_session()
    response = http_session.get(doi, headers=headers)
    response.raise_for_status()
    return response.json()


def fetch_bibliography(doi):
    style = 'ieee-with-url'
    style = 'apa'
    headers = {'Accept': 'text/bibliography; style=' + style}
    http_session = retrying_http_session()
    response = http_session.get(doi, headers=headers)
    response.raise_for_status()
    return response.text


def doi2fn(doi, collection_dir='_publication'):
    fn = urlparse(doi).path.lstrip('/').replace('/', '_')
    return '{0}/{1}.md'.format(collection_dir, fn)


def issued(csl):
    date_parts = csl['issued']['date-parts'][0]
    year = date_parts[0]
    try:
        month = date_parts[1]
    except IndexError:
        month = 1
    try:
        day = date_parts[2]
    except IndexError:
        day = 1

    dt = datetime(year, month, day)
    return dt.isoformat()


def docs_with_doi(doi, docs):
    """look in document list for doi fields
    and return project ids with the given doi
    """
    return [p[1]['@id'] for p in docs if 'doi' in p[1] and doi in p[1]['doi']]


def generate_publication(doi, endorsers, projects, docs):
    publication_fn = doi2fn(doi)
    if isfile(publication_fn):
        raise IOError(1, '`{0}` file already exists, remove it before regeneration'.format(publication_fn), publication_fn)

    uniq_projects = set(projects) | set(docs_with_doi(doi, docs))

    csl = fetch_csljson(doi)
    publication = {
        '@id': doi,
        'description': fetch_bibliography(doi),
        'author': list(uniq_projects),
        'endorsedBy': endorsers,
        'publishedIn': csl['container-title'],
        'type': csl['type'],
        'date': issued(csl),
    }
    publication_md = object2jekyll(publication, 'description')

    logging.info('Writing {0}'.format(publication_fn))
    with open(publication_fn, 'w') as fn:
        fn.write(publication_md)
