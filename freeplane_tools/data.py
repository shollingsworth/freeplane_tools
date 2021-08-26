#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mindmap Template."""
import pathlib

EXAMPLEDIR = pathlib.Path(__file__).parent.joinpath("examples")
DATADIR = pathlib.Path(__file__).parent.joinpath("data")


def get_template():
    return DATADIR.joinpath("template.mm").read_bytes()
