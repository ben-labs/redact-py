#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from glob import glob

from distutils.command.install import INSTALL_SCHEMES
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

with open('README.md') as fp:
    DESCRIPTION = fp.read()

# with open('requirements.txt') as fp:
#     REQUIRED = fp.read()

setup(
    name='redactor2',
    version='0.1.0',
    description=DESCRIPTION,
    author='Ben Quek',
    author_email='ben.quek@ben-labs.net',
    maintainer='Ben Quek',
    maintainer_email='ben.quek@ben-labs.net',
    url='https://github.com/ben-labs/redact-py',
    py_modules=['redact', 'redactor.redactor'],
    entry_points='''
        [console_scripts]
        redactor=redact:main
    '''
)
