
from __future__ import print_function
import os
import sys
import datetime
from docopt import docopt
import requests
import json
import jsonschema
import yaml
import logging
from estep import jekyllfile2object, json_serializer, __version__
from estep.validate import Validator


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

    def validator(self, schemadir):
        schema_uris = list(self.schemas().values())
        return Validator(schema_uris, schemadir)

    def schemas(self):
        schemas = {}
        for default in self.config['defaults']:
            schemas[default['scope']['type']] = default['values']['schema']
        return schemas

    def collections(self):
        collections = []
        for colname in self.config['collections'].keys():
            colschema = self.schemas()[colname]
            collection = Collection(colname, directory='_' + colname, schema=colschema)
            collections.append(collection)
        return collections


def validate(schemadir):
    config = Config()
    validator = config.validator(schemadir)
    nr_errors = 0
    for collection in config.collections():
        logging.info('Collection: %s', collection.name)
        for docname, document in collection.documents():
            nr_errors += validator.validate(docname, document)
    if nr_errors:
        logging.warning('%i error(s) found', nr_errors)
        sys.exit(1)


def main(argv=sys.argv[1:]):
    """
    Utility for estep website.

    Usage:
      estep validate [--schemadir=<dir>] [-v]

    Options:
      -h, --help            Show this screen.
      -v, --verbose         Show more output.
      --schemadir=<dir>     Use local schema directory instead of remote schemas

    """
    arguments = docopt(main.__doc__, argv, version=__version__)

    logging.basicConfig(format='%(message)s', level=logging.WARN)
    if arguments['--verbose']:
        logging.getLogger().setLevel(logging.DEBUG)

    if arguments['validate']:
        validate(schemadir=arguments['--schemadir'])


def recurseDirectory(directory, schemaType):
    obj = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            ext = os.path.splitext(filename)[1]
            if ext.lower() in ['.md', '.markdown', '.mdown']:
                path = os.path.join(dirpath, filename)
                obj.append((path, jekyllfile2object(path, schemaType=schemaType)))
    return obj

