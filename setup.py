#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import codecs
import sys

from vincode.version import __version__
sys.path.insert(0, '..')

setup(
    name='vincode',
    version=__version__,
    author='Artem Vlasov',
    author_email='root@proscript.ru',
    url='https://github.com/Yuego/vincode',
    download_url='https://github.com/Yuego/vincode/archive/{0}.tar.gz'.format(__version__),

    description='VIN-code parser',
    long_description=codecs.open('README.rst', encoding='utf8').read(),

    license='MIT license',
    install_requires=[
        'pyparsing',
        'dawg',
        'six',
    ],
    packages=find_packages(exclude=('tests', 'tests.*')),
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Russian',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
