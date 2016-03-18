#!/usr/bin/env python
# eStep
#
# Copyright 2015 Netherlands eScience Center
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""eStep utilities"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

exec(open('estep/version.py').read())

setup(name='estep',
      version=__version__,
      description=__doc__,
      author='Joris Borgdorff',
      author_email='j.borgdorff@esciencecenter.nl',
      url='https://github.com/eStep/eStep.github.io',
      packages=['estep'],
      install_requires=['docopt', 'PyYAML', 'python-frontmatter', 'jsonschema', 'requests'],
      tests_require=['nose', 'pyflakes', 'pep8', 'coverage'],
      entry_points={
        'console_scripts': [
            'estep = estep.script:main'
        ]
      },
      classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
      ],
      )
