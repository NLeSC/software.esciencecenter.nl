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
import logging
import yaml

from .utils import retrying_http_session

LOGGER = logging.getLogger('estep')


def fetch_bibliography(doi):
    style = 'ieee-with-url'
    style = 'apa'
    headers = {'Accept': 'text/bibliography; style=' + style}
    http_session = retrying_http_session()
    response = http_session.get(doi, headers=headers)
    response.raise_for_status()
    return response.text


def generate_publications(projects, publications_fn='_data/publication.yml'):
    # load existing publications
    orig_publications = []
    try:
        with open(publications_fn, 'r') as fn:
            orig_publications = yaml.load(fn)
    except IOError:
        pass

    # dois of projects
    dois = {}
    for docname, project in projects:
        if 'doi' in project:
            project_dois = project['doi']
            for doi in project_dois:
                if doi in dois:
                    dois[doi].append(project['@id'])
                else:
                    dois[doi] = [project['@id']]

    # keep publication which are in projects and for which the bibliography has already been fetched
    # to force bibliography fetching remove the `publications_fn` file.
    publications = []
    fetched_dois = set()
    for publication in orig_publications:
        doi = publication['@id']
        if doi in dois:
            LOGGER.debug('Not fetching bibliography of {0}, has already been fetched'.format(doi))
            publication['publishedBy'] = dois[doi]
            publications.append(publication)
            fetched_dois.add(publication['@id'])

    # fetch missing bibliographys
    dois_of_missing_bibliographys = set(dois.keys()) - fetched_dois
    for doi in dois_of_missing_bibliographys:
        LOGGER.info('Fetching bibliography of {0}'.format(doi))
        publication = {
            '@id': doi,
            'bibliography': fetch_bibliography(doi),
            'publishedBy': dois[doi],
        }
        publications.append(publication)

    # write publications
    with open(publications_fn, 'w') as fn:
        yaml.safe_dump(publications, fn, default_flow_style=False)

