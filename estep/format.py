import yaml
import json
import frontmatter
import os
import datetime


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, datetime.datetime) or isinstance(obj, datetime.date) or isinstance(obj, datetime.time):
        serial = obj.isoformat()
        return serial
    raise TypeError ("Type not serializable: " + str(obj))


def object2jekyll(data, contentProperty):
    """
    Converts a dict to a Jekyll template, with YAML metadata and Markdown content
    :param data: dict with data that will be dumped
    :param contentProperty: property name of data that contains the Markdown content
    :return: string containing a Jekyll template
    """
    d = {}
    for key, value in data.items():
        if key == contentProperty:
            continue

        key = key.lstrip('@')
        d[key] = value

    metadata = yaml.safe_dump(d, default_flow_style=False)

    content = data[contentProperty]
    return "---\n{0}\n---\n{1}".format(metadata, content)


def jekyllfile2object(filename, schemaType=None, contentProperty='description', uriPrefix='http://estep.esciencecenter.nl'):
    with open(filename) as f:
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
    return obj

def jekyll2json(filename, outputDir, contentProperty='description'):
    """
    Converts a Jekyll file to JSON and saves it in given output directory. It uses the contentProperty property to
    set

    """
    with open(filename, 'r') as f:
        dataString = f.read()

    obj = jekyll2object(dataString, contentProperty)

    last_id_part = obj['@id'].rindex('/') + 1
    fname = os.path.join(outputDir, obj['@id'][last_id_part:] + '.json')
    with open(fname, 'w') as f:
        json.dump(obj, f)
