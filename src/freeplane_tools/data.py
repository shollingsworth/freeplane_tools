#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Static Data methods."""
import pathlib

DATADIR = pathlib.Path(__file__).resolve().parent.joinpath("data")
"""Package Data directory."""


def get_template():
    """Return data from template."""
    return DATADIR.joinpath("template.mm").read_bytes()
