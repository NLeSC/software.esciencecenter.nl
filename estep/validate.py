"""Validator

Usage:
  validate.py <json>
"""
import json
import jsonschema
import os

from docopt import docopt


def main(argv=sys.argv[1:]):
    # TODO implement read all collection markdown files, convert to json and validate against schema of collection
    pass


if __name__ == '__main__':
    args = docopt(__doc__)

    jsonFile = args['<json>']
    myJson = json.load(open(jsonFile, 'r'))

    schemas = {
        'http://estep.esciencecenter.nl/schema/person': 'NLeSC_person_schema.json',
        'http://estep.esciencecenter.nl/schema/organization': 'NLeSC_organization_schema.json',
        'http://estep.esciencecenter.nl/schema/project': 'NLeSC_project_schema.json',
        'http://estep.esciencecenter.nl/schema/software': 'NLeSC_software_schema.json'
    }

    schemaFile = schemas[myJson['schema']]
    print "Schemafile: " + schemaFile
    mySchema = json.load(open(schemaFile, 'r'))
    print 'loaded ok'

    try:
        cwd = os.getcwd()
        resolver = jsonschema.RefResolver('file://' + cwd + '/' + schemaFile, mySchema)
        jsonschema.Draft4Validator(mySchema, resolver=resolver).validate(myJson)
        print 'OK'
    except jsonschema.SchemaError as ex:
        print 'Schema error...'
        raise EnvironmentError(ex.message)
    except jsonschema.ValidationError as ex:
        print 'Validation error...'
        raise ValueError(ex.message)
