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

from docopt import docopt
import yaml
from .format import jekyllfile2object, object2jekyll
from .validate import Validator, AbstractValidators, url_to_path, url_to_collection_name, load_schemas
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
        return recurseDirectory(self.directory, self.name)


class Config(object):
    def __init__(self, filename='_config.yml'):
        with open(filename) as f:
            self.config = yaml.load(f)

    def validator(self, schemadir, resolve_local, resolve_remote):
        return Validator(self.schema_uris(), schemadir, resolve_local, resolve_remote)

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


def validate(schemadir, resolve_local=True, resolve_remote=False):
    config = Config()
    validator = config.validator(schemadir, resolve_local, resolve_remote)
    nr_errors = 0
    for collection in config.collections():
        LOGGER.info('Collection: %s', collection.name)
        for docname, document in collection.documents():
            nr_errors += validator.validate(docname, document)
    LOGGER.info('--------------------------')
    nr_errors += validator.finalize()
    if nr_errors:
        LOGGER.warning('%i error(s) found', nr_errors)
        sys.exit(1)
    else:
        LOGGER.info('No errors found')


def generate_reciprocal():
    config = Config()
    validator = AbstractValidators(relationship.get_validators())

    nr_errors = 0
    for collection in config.collections():
        LOGGER.info('Collection: %s', collection.name)
        for docname, document in collection.documents():
            nr_errors += validator.validate(docname, document)

    schemas = load_schemas(config.schema_uris())

    if nr_errors > 0:
        faulty_docs = {}
        for (url, property_name, value) in validator.missing():
            LOGGER.debug("* Found missing relationship {0}#{1}: {2}".format(url, property_name, value))
            if url not in faulty_docs:
                path = url_to_path(url)
                collection_name = url_to_collection_name(url)
                try:
                    faulty_docs[url] = jekyllfile2object(path, schemaType=collection_name)
                except IOError as ex:
                    LOGGER.warning("Cannot read path %s to fix missing relationship %s#%s: %s", path, url, property_name, value)
                    continue

            doc = faulty_docs[url]
            schema = schemas[doc['schema']]
            LOGGER.error((url, property_name, value, schema))
            if schema['properties'][property_name]['type'] == 'array':
                if property_name not in doc:
                    doc[property_name] = []
                doc[property_name].append(value)
            else:
                doc[property_name] = value


        for url, document in faulty_docs.items():
            path = url_to_path(url)
            LOGGER.info("Writing fixed file %s", path)
            with open(path, 'w') as f:
                f.write(object2jekyll(document, 'description'))

        LOGGER.warning('Fixed %d missing relationships in %d documents', nr_errors, len(faulty_docs))


def main(argv=sys.argv[1:]):
    """
    Utility for estep website.

    Available commands:
      validate                Validates content.
      generate reciprocal     Checks that relationships are bi-directional and generates the missing ones.

    Usage:
      estep validate [--local] [--resolve] [--no-local-resolve] [-v | -vv]
      estep generate reciprocal [-v | -vv]

    Options:
      -h, --help              Show this screen.
      -v, --verbose           Show more output.
      -l, --local             Use local schemas instead of remote schemas
      -R, --no-local-resolve  Do not resolve local URLs
      -r, --resolve           Resolve remote URLs
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
                 resolve_local=not arguments['--no-local-resolve'])
    elif arguments['generate'] and arguments['reciprocal']:
        generate_reciprocal()


def recurseDirectory(directory, schemaType):
    obj = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            ext = os.path.splitext(filename)[1]
            if ext.lower() in ['.md', '.markdown', '.mdown']:
                path = os.path.join(dirpath, filename)
                obj.append((path, jekyllfile2object(path, schemaType=schemaType)))
    return obj
