#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='ts_dweepy',
    version='0.3.0',
    description='TS_Dweepy is a Python client for dweet.io on ThingSpace',
    long_description=open('README.rst').read(),
    author='Jeff Irland',
    author_email='jeffskinnerbox@yahoo.com',
    url='https://github.com/jeffskinnerbox/ts_dweepy',
    packages=[
        'ts_dweepy',
    ],
    package_dir={'ts_dweepy':
                 'ts_dweepy'},
    include_package_data=True,
    install_requires=['requests >= 2, < 3'],
    license="MIT",
    zip_safe=False,
    keywords='ts_dweepy dweepy dweet dweet.io',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    test_suite='tests_ts_dweepy',
)
