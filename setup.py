# -*- coding: utf-8 -*-

import os
import re
import sys

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_version(package):
    """Return package version as listed in `__version__` in `__init__.py`."""
    init_py = open(os.path.join(os.path.dirname(__file__),
                                package, '__init__.py'),
                   'r').read()
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]",
                     init_py, re.MULTILINE
                     ).group(1)




setup(
    name='pyboleto',
    version=get_version('pyboleto'),
    author='Eduardo Cereto Carvalho',
    author_email='eduardocereto@gmail.com',
    url='https://github.com/eduardocereto/pyboleto',
    packages=find_packages(),
    package_data={
        '': ['LICENSE'],
        'pyboleto': ['media/*.jpg', 'templates/*.html'],
        'tests': ['xml/*.xml']
    },
    zip_safe=False,
    provides=[
        'pyboleto'
    ],
    license='BSD',
    description='Python Library to create "boletos de cobrança bancária" for \
    several Brazilian banks',
    long_description=read('README.rst'),
    download_url='http://pypi.python.org/pypi/pyboleto',
    scripts=[
        'bin/html_pyboleto_sample.py',
        'bin/pdf_pyboleto_sample.py'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Topic :: Office/Business :: Financial',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms='any',
    test_suite='tests.alltests.suite',
    install_requires=[
        'setuptools',
        'reportlab'
    ]
)
