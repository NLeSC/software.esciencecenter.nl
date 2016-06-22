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
from .utils import url_to_path, url_to_collection_name, parse_url
from .version import __version__
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
        docs = []
        for dirpath, dirnames, filenames in os.walk(self.directory):
            for filename in filenames:
                ext = os.path.splitext(filename)[1]
                if ext.lower() in ['.md', '.markdown', '.mdown']:
                    path = os.path.join(dirpath, filename)
                    docs.append((path, jekyllfile2object(path, schemaType=self.name)))
        return docs


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
        collections = []
        for colname in sorted(self.config['collections'].keys()):
            colschema = self.schemas()[colname]
            collection = Collection(colname, directory='_' + colname, schema=colschema)
            collections.append(collection)
        return collections


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


def generate_reciprocal():
    config = Config()
    validator = Validators(relationship.get_validators())

    LOGGER.info('Parsing documents')
    for collection in config.collections():
        LOGGER.info('Collection: %s', collection.name)
        for docname, document in collection.documents():
            LOGGER.debug('Document: %s', docname)
            # Must loop over whole iterator, otherwise no items are stored.
            list(validator.iter_errors(document))

    schemas = load_schemas(config.schema_uris())

    missings = list(validator.missing())
    nr_errors = len(missings)
    if nr_errors > 0:
        faulty_docs = {}
        for (url, property_name, value) in missings:
            LOGGER.debug("* Found missing relationship {0}#{1}: {2}".format(url, property_name, value))
            if url not in faulty_docs:
                path = url_to_path(parse_url(url))
                collection_name = url_to_collection_name(url)
                try:
                    faulty_docs[url] = jekyllfile2object(path, schemaType=collection_name)
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
            path = url_to_path(url)
            LOGGER.info("Writing fixed file %s", path)
            with codecs.open(path, encoding='utf-8', mode='w') as f:
                f.write(object2jekyll(document, 'description'))

        LOGGER.warning('Fixed %d missing relationships in %d documents', nr_errors, len(faulty_docs))
    else:
        LOGGER.warning('Everything is OK, no missing relationships found')


def main(argv=sys.argv[1:]):
    """
    Utility for estep website.

    Available commands:
      validate                Validates content.
      generate reciprocal     Checks that relationships are bi-directional and generates the missing ones.

    Usage:
      estep validate [--local] [--resolve] [--resolve-cache-expire=<days>] [--no-local-resolve] [-v | -vv] [<schema_type> <file>]
      estep generate reciprocal [-v | -vv]

    Options:
      -h, --help                     Show this screen.
      -v, --verbose                  Show more output.
      -l, --local                    Use local schemas instead of remote schemas
      -R, --no-local-resolve         Do not resolve local URLs
      -r, --resolve                  Resolve remote URLs
      --resolve-cache-expire=<days>  Timeout in days after the resolve cache expires, use 0 to disable cache [default: 14].
      <schema_type>                  One of (person, software, organization, project)
      <file>                         Single file to validate
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
    elif arguments['generate'] and arguments['reciprocal']:
        generate_reciprocal()
