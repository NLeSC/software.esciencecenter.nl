import datetime

import jsonschema
import requests
from .util import module_dirpath
import os
import json
import logging


def local_schema_store(base_uri='http://estep.esciencecenter.nl/schema/'):
    """
    Loads the schemas from the local module.

    :param base_uri: URI to prefix schema with.
    :return: dict with the file uri and the base_uri both pointing to the local schema.
    """
    store = {}
    base_path = os.path.abspath(os.path.join(module_dirpath(), '..', 'schema'))
    for filename in os.listdir(base_path):
        if os.path.splitext(filename.lower())[1] != '.json':
            continue

        filepath = os.path.join(base_path, filename)
        with open(filepath) as f:
            schema = json.load(f)
        store['file://' + filepath] = schema
        store[base_uri + filename] = schema
        store[base_uri + os.path.splitext(filename)[0]] = schema
    return store


class Validator(object):
    def __init__(self, schema_uris, schemadir=None):
        store = {}
        for schema_uri in schema_uris:
            if schemadir is None:
                u = schema_uri
                # TODO remove replace when domains are fixed
                u = u.replace('estep.esciencecenter.nl', 'estep.github.io')
                request = requests.get(u)
                # do not accept failed calls
                try:
                    request.raise_for_status()
                except requests.exceptions.HTTPError as ex:
                    logging.error("cannot load schema %s:\n\t%s\nUse --schemadir=schema to load local schemas.".format(schema_uri, ex))

                store[schema_uri] = request.json()
            else:
                logging.debug('Loading schema %s from %s', schema_uri, schemadir)
                schema_fn = schema_uri.replace('http://estep.esciencecenter.nl/schema', schemadir)
                with open(schema_fn) as f:
                    store[schema_uri] = json.load(f)

        # Resolve date-time as dates as well as strings
        if isinstance(jsonschema.compat.str_types, type):
            str_types = [jsonschema.compat.str_types]
        else:
            str_types = list(jsonschema.compat.str_types)
        str_types.append(datetime.date)
        types = {u'string': tuple(str_types)}

        self.validators = {}
        for schema_uri in schema_uris:
            schema = store[schema_uri]
            resolver = jsonschema.RefResolver(schema_uri, schema,  store=store)
            self.validators[schema_uri] = jsonschema.Draft4Validator(schema, resolver=resolver, types=types)

    def validate(self, name, instance):
        schema_uri = instance['schema']
        errors = list(self.validators[schema_uri].iter_errors(instance))
        has_errors = len(errors) == 0
        if has_errors:
            logging.info('Document: %s OK', name)
        else:
            logging.warning ('Document: %s BAD (schema:%s)\n-------------------------------------------------\n', name, schema_uri)
            for error in errors:
                logging.warning(error)
            logging.warning ('-------------------------------------------------')
        return len(errors)
