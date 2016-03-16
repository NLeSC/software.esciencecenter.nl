"""Validator

Usage:
  validate.py <json>
"""
import os

import json
import yaml
import jsonschema

from estep.format import jekyllfile2object


def main():
    """
    :param argv:
    :return:

    Read all collection markdown files, convert to json and validate against schema of collection
    """
    schemaUrlBase = 'http://estep.esciencecenter.nl/schema/'
    schemaFileBase = '/schema/'

    collections = []
    with open('_config.yml') as f:
        config = yaml.load(f)
        collections = config['collections'].keys()

    cwd = os.getcwd()
    for collection in sorted(collections):
        print('Collection: ' + collection)
        schemaFile = cwd + schemaFileBase + collection
        schema = json.load(open(schemaFile, 'r'))

        print('Validating against: ' + schemaFile)
        schemaStore = {}
        resolver = jsonschema.RefResolver('file://' + schemaFile, schema, store=schemaStore)
        validator = jsonschema.Draft4Validator(schema, resolver=resolver)

        collectionDir = cwd + '/' + '_' + collection + '/'
        for mdfile in os.listdir(collectionDir):
            try:
                print(mdfile, end=" ")
                myJson = jekyllfile2object(collectionDir + mdfile, collection)
                validator.validate(myJson)
                print('OK')
            except jsonschema.ValidationError as ex:
                print('Validation error...')
                raise ValueError(ex.message)
