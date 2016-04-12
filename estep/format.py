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

import datetime
import os
import json
import codecs

import yaml
import frontmatter


def json_serializer(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, datetime.datetime) or isinstance(obj, datetime.date) or isinstance(obj, datetime.time):
        serial = obj.isoformat()
        return serial
    raise TypeError("Type not serializable: " + str(obj))


def object2jekyll(data, contentProperty):
    """
    Converts a dict to a Jekyll template, with YAML metadata and Markdown content
    :param data: dict with data that will be dumped
    :param contentProperty: property name of data that contains the Markdown content
    :return: string containing a Jekyll template
    """
    d = {}
    for key, value in data.items():
        if key in (contentProperty, '@id', 'schema'):
            continue

        d[key] = value

    metadata = yaml.safe_dump(d, default_flow_style=False)

    content = data[contentProperty]
    try:
        return "---\n{0}---\n{1}\n".format(metadata, content)
    except UnicodeEncodeError:
        return unicode("---\n{0}---\n{1}\n").format(unicode(metadata), unicode(content)).encode('UTF-8')


def jekyllfile2object(filename, schemaType=None, contentProperty='description', uriPrefix='http://software.esciencecenter.nl'):
    """
    Converts a Jekyll file to a python dict. The schema and @id properties are deduced from
    """
    with codecs.open(filename, encoding='UTF-8') as f:
        obj = jekyll2object(f.read(), contentProperty)

    fullpath = os.path.abspath(filename)
    path, filename = os.path.split(fullpath)
    name = os.path.splitext(filename)[0]
    if schemaType is None:
        schemaType = os.path.basename(path)

    if '@id' not in obj:
        obj['@id'] = uriPrefix + '/' + schemaType + '/' + name

    if 'schema' not in obj:
        obj['schema'] = uriPrefix + '/schema/' + schemaType

    return obj


def jekyll2object(dataString, contentProperty='description'):
    """
    Converts a Jekyll template string to a metadata dict and content string. See python-frontmatter package for more
    documentation.
    :param dataString: template as a string
    :return: a tuple of (metadata, content)
    """
    fm = frontmatter.loads(dataString)
    obj = dict(fm.metadata)
    if contentProperty in obj:
        raise ValueError('The content property {0} is already defined, cannot override'.format(contentProperty))

    # convert id to JSON-LD
    if 'id' in obj:
        obj['@id'] = obj['id']
        del obj['id']

    obj[contentProperty] = fm.content

    return convert_empty(obj)


def convert_empty(value):
    if isinstance(value, dict):
        return remove_empty_from_dict(value)
    elif isinstance(value, (list, tuple)):
        return remove_empty_from_list(value)
    else:
        return value


def remove_empty_from_dict(obj):
    updated = {}
    for key, value in obj.items():
        new_value = convert_empty(value)
        if new_value is not None:
            updated[key] = new_value

    return updated


def remove_empty_from_list(obj):
    updated = []
    for value in obj:
        new_value = convert_empty(value)
        if new_value is not None:
            updated.append(new_value)
    return updated


def jekyll2json(filename, outputDir, contentProperty='description'):
    """
    Converts a Jekyll file to JSON and saves it in given output directory.
    """
    with codecs.open(filename, encoding='utf-8') as f:
        dataString = f.read()

    obj = jekyll2object(dataString, contentProperty)

    last_id_part = obj['@id'].rindex('/') + 1
    fname = os.path.join(outputDir, obj['@id'][last_id_part:] + '.json')
    with codecs.open(fname, encoding='utf-8', mode='w') as f:
        json.dump(obj, f)
