#!/usr/bin/env python

from setuptools import setup, find_packages

# parse version string from the __init__ file
with open("records/__init__.py", "r") as initfile:
    lines = initfile.readlines()
    for line in lines:
        if "__version__" in line:
            # get version line and strip white space and quotations
            version = line.strip().split()[-1].strip("'").strip('"')

setup(
    name="records",
    version="0.2",
    packages=find_packages(),
    author="Ilana Z Rubin",
    author_email="izr2000@columbia.edu",
    license="GPLv3",
    description="A package to query GBIF for taxon occurrence records",
    classifiers=["Programming Language :: Python :: 3"],
)
