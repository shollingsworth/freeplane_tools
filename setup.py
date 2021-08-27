#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup
from glob import glob
from itertools import chain

SCRIPTS = [
    i
    for i in chain(
        glob("bin/*.py"),
        glob("bin/*.sh"),
    )
]

setup(
    name="freeplane_tools",
    install_requires=[
        "beautifulsoup4 >= 4.8.2",
        "lxml >= 4.5.0",
    ],
    scripts=SCRIPTS,
)
