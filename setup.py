#!/usr/bin/env python
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

config = {
    'description': 'text file to emoji',
    'author': 'Jason French',
    'url': 'https://github.com/JasonLeeFrench/pictopythocryptography',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['pictopythocryptography'],
    'name': 'pictopythocryptography',
    'long_description':read('README.md'),
    'entry_points': {
      'console_scripts': [
        'pictopythocryptography=pictopythocryptography:main'
      ]
    }
}

setup(**config)
