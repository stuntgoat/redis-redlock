#!/usr/bin/env python

from distutils.core import setup

from version import version

dependencies = ['redis']


setup(
    name='redlock',
    version=version,
    description='Redlock for python',
    url='https://github.com/stuntgoat/redis-redlock',
    author='@stuntgoat',
    packages=['redlock'],
    install_requires=dependencies,
    long_description=open('README.md').read(),
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
)
