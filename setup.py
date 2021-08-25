#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from glob import glob
import os

DIR = os.path.dirname(__file__)
FILE_REQ = os.path.join(DIR, "requirements.txt")
REQUIRES = [i.strip() for i in open(FILE_REQ).readlines()]
INFO = {
    "name": "Steven Hollingsworth",
    "email": "hollingsworth.stevend@gmail.com",
    "url": "https://github.com/shollingsworth/freeplane_tools",
}

DESCRTIPTION = """
This package provides some tooling around translating freeplane mindmap files
into other useful formats
""".strip()

setup(
    name="freeplane_tools",
    version="0.0.1",
    license="MIT",
    description=DESCRTIPTION,
    packages=find_packages(),
    install_requires=REQUIRES,
    package_data={"": ["data/*"]},
    keywords=[
        "freeplane",
        "mindmap",
        "markdown",
    ],
    scripts=glob("bin/*.py") + glob("bin/*.sh"),
    url=INFO["url"],
    maintainer=INFO["name"],
    maintainer_email=INFO["email"],
    include_package_data=True,
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Development Status :: 3 - Alpha",
        # Define that your audience are developers
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        # Again, pick a license
        "License :: OSI Approved :: MIT License",
        # Specify which pyhton versions that you want to support
        "Programming Language :: Python :: 3",
    ],
)
