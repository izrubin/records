#!/usr/bin/env python

from setuptools import setup, find_packages
setup(
    name="records",
    version="0.1",
    packages=find_packages(),
    author="Ilana Z Rubin",
    license="GPLv3",
    description="A package to query GBIF for taxon occurrence records",
    classifiers=["Programming Language :: Python :: 3"],
)