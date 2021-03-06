#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='gitzen',
    version='0.1.0',
    description='Git Zen',
    long_description=readme + '\n\n' + history,
    author='Ian McCracken',
    author_email='ian.mccracken@gmail.com',
    url='https://github.com/iancmcc/gitzen',
    packages=[
        'gitzen',
    ],
    package_dir={'gitzen': 'gitzen'},
    include_package_data=True,
    install_requires=[
        "py",
        "gitflow",
        "requests",
    ],
    entry_points="""
    [console_scripts]
    git-zen = gitzen.gitzen:main
    """,
    license="BSD",
    zip_safe=False,
    keywords='gitzen',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
)