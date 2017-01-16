#!/kweezyenv/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import codecs

from setuptools import setup

try:
    # Python 3
    from os import dirname
except ImportError:
    # Python 2
    from os.path import dirname

here = os.path.abspath(dirname(__file__))

with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

setup(
    name='kweezelbotter',
    version='0.0.1',
    description='A tool for pronouncing words',
    long_description=long_description,
    url='https://github.com/ncmatson/kweezelbotter',
    license='MIT',
)
