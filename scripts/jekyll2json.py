#!/usr/bin/env python

"""
Converts Jekyll markdown files with metadata to a JSON object.

If a directory is given, it recursively searches for all files with an .md extension. Those are all combined in a
single JSON array object. If a file is given, it writes the single file. If no input is given, the current directory
is searched for markdown files.

Usage:
  jekyll2json.py <output>
  jekyll2json.py <input> <output>

Arguments:
  <input>               Input file or directory
  <output>              JSON output file

Options:
  -h, --help            Show this screen.
  -v, --verbose         Show more output.
"""

from estep.format import jekyllfile2object, json_serial
import docopt
import os
import json


def recurseDirectory(directory):
    obj = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            ext = os.path.splitext(filename)[1]
            if ext.lower() in ['.md', '.markdown', '.mdown']:
                path = os.path.join(dirpath, filename)
                obj.append(jekyllfile2object(path))
    return obj


def main(opts):
    if opts['<input>'] is not None:
        if os.path.isfile(opts['<input>']):
            obj = jekyllfile2object(opts['<input>'])
        else:
            obj = recurseDirectory(opts['<input>'])
    else:
        obj = {
            'projects': recurseDirectory('project'),
            'software': recurseDirectory('software'),
            'persons': recurseDirectory('person'),
            'organizations': recurseDirectory('organization'),
        }

    with open(opts['<output>'], 'w') as f:
        json.dump(obj, f, default=json_serial)

if __name__ == '__main__':
    opts = docopt.docopt(__doc__)
    main(opts)
