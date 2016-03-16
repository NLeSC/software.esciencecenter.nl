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

"""
Internal setup of the xenon package.

Use make install instead for correct dependency detection.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from glob import glob
import os

setup(name='estep',
      version='0.1.0',
      description='eStep utilities.',
      author='Joris Borgdorff',
      author_email='j.borgdorff@esciencecenter.nl',
      url='https://github.com/eStep/eStep',
      packages=['estep'],
      install_requires=['docopt', 'PyYAML', 'python-frontmatter'],
      tests_require=['nose', 'pyflakes', 'pep8', 'coverage'],
      entry_points={
        'console_scripts': [
            'validate_estep = estep.validate.main'
        ]
      }
     )
