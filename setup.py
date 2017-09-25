#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='fast_mises',
    version='0.0.0',
    description='Fast von Mises function fit.',
    author='Dimitri Yatsenko',
    packages=find_packages(exclude=[]),
    install_requires=['numpy'],
)
