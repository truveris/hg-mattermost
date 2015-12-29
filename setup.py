# Copyright 2015-2016, Truveris Inc. All Rights Reserved.

import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, "README.rst")).read()
    CHANGES = open(os.path.join(here, "CHANGES.txt")).read()
except IOError:
    README = CHANGES = ""

setup(
    name="hg-mattermost",
    version="0.1",
    description="Mercurial to Mattermost hook",
    long_description=README + "\n\n" + CHANGES,
    author="Truveris Inc.",
    author_email="engineering@truveris.com",
    url="https://github.com/truveris/hg-mattermost",
    license="LICENSE",
    install_requires=[
        "requests",
        "hgapi",
    ],
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Topic :: Software Development :: Version Control",
    ],
    scripts=[
        "hg-mattermost",
    ],
    packages=find_packages(),
)
