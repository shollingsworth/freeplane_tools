#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup
from glob import glob


setup(
    name="freeplane_tools",
    install_requires=[
        "beautifulsoup4",
        "lxml",
    ],
    scripts=list(glob("./bin/*.py")) + list(glob("./bin/*.sh")),
)
