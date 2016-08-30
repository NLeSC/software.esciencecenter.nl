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
import os
import sys
import logging
import codecs

from docopt import docopt
import yaml

from .format import jekyllfile2object, object2jekyll
from .validate import Validators, EStepValidator, log_error
from .schema import load_schemas
from .utils import (url_to_path, url_to_collection_name, parse_url,
    is_internal_url, download_file)
from .version import __version__
from .publication import generate_publication
from . import relationship

LOGGER = logging.getLogger('estep')


class Collection(object):
    name = ''
    directory = ''
    schema = ''

    def __init__(self, name, directory, schema):
        self.name = name
        self.directory = directory
        self.schema = schema

    def documents(self):
        for dirpath, dirnames, filenames in os.walk(self.directory):
            for filename in filenames:
                ext = os.path.splitext(filename)[1]
                if ext == '.md':
                    path = os.path.join(dirpath, filename)
                    yield (path, jekyllfile2object(path, schemaType=self.name))


class Config(object):
    def __init__(self, filename='_config.yml'):
        with open(filename) as f:
            self.config = yaml.load(f)

    def validator(self, schemadir, resolve_local, resolve_remote, resolve_cache_expire=5):
        return EStepValidator(self.schema_uris(), schemadir, resolve_local, resolve_remote,
                              resolve_cache_expire=resolve_cache_expire)

    def schemas(self):
        schemas = {}
        for default in self.config['defaults']:
            schemas[default['scope']['type']] = default['values']['schema']
        return schemas

    def schema_uris(self):
        return list(self.schemas().values())

    def collections(self):
        for colname in sorted(self.config['collections'].keys()):
            colschema = self.schemas()[colname]
            collection = Collection(colname, directory='_' + colname, schema=colschema)
            yield collection

    def documents(self):
        for collection in self.collections():
            for path, document in collection.documents():
                yield collection.name, path, document


def validate_document(validator, document):
    docid = document['@id']
    docfn = url_to_path(parse_url(docid))

    errors = list(validator.iter_errors(document))
    nr_errors = len(errors)
    has_errors = nr_errors == 0
    if has_errors:
        LOGGER.info('Document: %s OK', docfn)
    else:
        warning_msg = 'Document: {0} BAD'.format(docfn)
        separator = '-' * len(warning_msg)
        LOGGER.warning(separator)
        LOGGER.warning(warning_msg)
        LOGGER.warning(separator + '\n')
        for error in errors:
            log_error(error)
    return nr_errors


def validate(schemadir, resolve_local=True, resolve_remote=False, path=None, schema_type=None, resolve_cache_expire=5):
    config = Config()
    validator = config.validator(schemadir, resolve_local, resolve_remote, resolve_cache_expire=resolve_cache_expire)

    nr_errors = 0
    if path is None:
        for collection in config.collections():
            LOGGER.info('Collection: %s', collection.name)
            for docname, document in collection.documents():
                nr_errors += validate_document(validator, document)
    else:
        document = jekyllfile2object(path, schemaType=schema_type)
        nr_errors += validate_document(validator, document)

    errors = list(validator.finalize())
    nr_errors += len(errors)
    if len(errors) == 0:
        LOGGER.info('Relationships: OK')
    else:
        LOGGER.info('Relationships: BAD')
        for error in errors:
            log_error(error)

    if nr_errors:
        LOGGER.warning('%i error(s) found', nr_errors)
        sys.exit(1)
    else:
        LOGGER.warning('No errors found')


def generate_reciprocal(schemadir):
    config = Config()
    validator = Validators(relationship.get_validators())

    LOGGER.info('Parsing documents')
    for collection in config.collections():
        LOGGER.info('Collection: %s', collection.name)
        for docname, document in collection.documents():
            LOGGER.debug('Document: %s', docname)
            # Must loop over whole iterator, otherwise no items are stored.
            list(validator.iter_errors(document))

    schemas = load_schemas(config.schema_uris(), schemadir)

    missings = list(validator.missing())
    nr_errors = len(missings)
    if nr_errors > 0:
        faulty_docs = {}
        for (url, property_name, value) in missings:
            LOGGER.debug("* Found missing relationship {0}#{1}: {2}"
                         .format(url, property_name, value))
            if url not in faulty_docs:
                parsed_url = parse_url(url)
                path = url_to_path(parsed_url)
                collection_name = url_to_collection_name(parsed_url)
                try:
                    faulty_docs[url] = jekyllfile2object(
                        path, schemaType=collection_name)
                except IOError:
                    LOGGER.warning("Cannot read path %s to fix missing "
                                   "relationship %s#%s: %s", path, url,
                                   property_name, value)
                    continue

            doc = faulty_docs[url]
            schema = schemas[doc['schema']]

            if ('type' in schema['properties'][property_name] and
                    schema['properties'][property_name]['type'] == 'array'):
                if property_name not in doc:
                    doc[property_name] = []
                if value not in doc[property_name]:
                    doc[property_name].append(value)
            else:
                doc[property_name] = value

        for url, document in faulty_docs.items():
            path = url_to_path(parse_url(url))
            LOGGER.info("Writing fixed file %s", path)
            with codecs.open(path, encoding='utf-8', mode='w') as f:
                f.write(object2jekyll(document, 'description'))

        LOGGER.warning('Fixed %d missing relationships in %d documents',
                       nr_errors, len(faulty_docs))
    else:
        LOGGER.warning('Everything is OK, no missing relationships found')


def sort_document_properties():
    """ Regenerate all files, causes the attributes to be sorted. This reduces merge conflicts. """
    config = Config()

    LOGGER.info('Parsing documents')
    for collection in config.collections():
        LOGGER.info('Collection: %s', collection.name)
        for path, document in collection.documents():
            LOGGER.info("Writing fixed file %s", path)
            with codecs.open(path, encoding='utf-8', mode='w') as f:
                f.write(object2jekyll(document, 'description'))
    LOGGER.warning('Done')


def generate_logo():
    config = Config()

    logo_name = {
        'organization': 'logo',
        'person': 'photo',
        'project': 'logo',
        'software': 'logo',
        'report': 'cover',
    }

    LOGGER.info('Parsing documents')
    success = 0
    failed = 0

    for collection, doc_path, document in config.documents():
        if collection not in logo_name:
            continue

        logo = logo_name[collection]
        LOGGER.debug('Document: %s', doc_path)

        if logo in document and not is_internal_url(parse_url(document[logo])):
            name = os.path.splitext(os.path.basename(doc_path))[0]
            base_path = os.path.join('images', collection, name)
            logo_url = document[logo]

            try:
                logo_path = download_file(logo_url, base_path)
                document[logo] = '/' + logo_path

                with codecs.open(doc_path, encoding='utf-8', mode='w') as f:
                    f.write(object2jekyll(document, 'description'))
                LOGGER.info("Downloaded logo {} to {} for {}"
                            .format(logo_url, logo_path, doc_path))
                success += 1
            except IOError:
                LOGGER.warning("Failed to download logo {} of {}"
                            .format(logo_url, doc_path))
                failed += 1
    if failed == 0 and success == 0:
        LOGGER.warning("No new images downloaded")
    else:
        LOGGER.warning("Images downloaded: {0} succeeded and {1} failed"
                       .format(success, failed))


def main(argv=sys.argv[1:]):
    """
    Utility for estep website.

    Available commands:
      validate                Validates content.
      generate reciprocal     Checks that relationships are bi-directional and generates the missing ones.
      generate publication    Generates publication Markdown file in _publication/ directory.
      generate logo           Downloads logos and puts the local files in the Markdown file
      sort                    Sorts all YAML properties, to make git merges easier.

    Usage:
      estep validate [--local] [--resolve] [--resolve-cache-expire=<days>] [--no-local-resolve] [-v | -vv] [<schema_type> <file>]
      estep generate reciprocal [--local] [-v | -vv]
      estep generate publication [-v | -vv] [--endorser=<endorser>]... [--project=<project>]... <doi>
      estep generate logo [-v | -vv]
      estep sort [-v | -vv]

    Options:
      -h, --help                     Show this screen.
      -v, --verbose                  Show more output.
      -l, --local                    Use local schemas instead of remote schemas
      -R, --no-local-resolve         Do not resolve local URLs
      -r, --resolve                  Resolve remote URLs
      --resolve-cache-expire=<days>  Timeout in days after the resolve cache expires, use 0 to disable cache [default: 14].
      --endorser=<endorser>          Endorser of publication [default: NLeSC].
      --project=<project>            Project responsible for publication. Format is an url like http://software.esciencecenter.nl/project/eMetabolomics
      <schema_type>                  One of (person, software, organization, project)
      <file>                         Single file to validate
      <doi>                          DOI of publication. Format is an url like http://dx.doi.org/10.1002/rcm.6364
    """
    arguments = docopt(main.__doc__, argv, version=__version__)

    logging.basicConfig(format='%(message)s', level=logging.WARN)
    if arguments['--verbose'] > 1:
        LOGGER.setLevel(logging.DEBUG)
    elif arguments['--verbose'] > 0:
        LOGGER.setLevel(logging.INFO)

    if arguments['validate']:
        schemadir = None
        if arguments['--local']:
            schemadir = 'schema'
        validate(schemadir=schemadir,
                 resolve_remote=arguments['--resolve'],
                 resolve_cache_expire=int(arguments['--resolve-cache-expire']),
                 resolve_local=not arguments['--no-local-resolve'],
                 path=arguments['<file>'],
                 schema_type=arguments['<schema_type>'],
                 )
    elif arguments['sort']:
        sort_document_properties()
    elif arguments['generate']:
        if arguments['reciprocal']:
            schemadir = None
            if arguments['--local']:
                schemadir = 'schema'
            generate_reciprocal(schemadir=schemadir)
        elif arguments['logo']:
            generate_logo()
        elif arguments['publication']:
            project_collection = [c for c in Config().collections() if c.name == 'project'][0]
            generate_publication(arguments['<doi>'],
                                 endorsers=arguments['--endorser'],
                                 projects=arguments['--project'],
                                 docs=project_collection.documents(),
                                 )
