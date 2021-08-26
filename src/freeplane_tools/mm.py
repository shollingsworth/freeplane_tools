#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mindmap Interface."""
from typing import Iterable
from bs4 import Tag, BeautifulSoup


class Mindmap(object):
    """Mindmap File Interface."""

    def __init__(self, srcfile):
        with open(srcfile) as fileh:
            content = fileh.read()
        self.content = content
        self.xml = BeautifulSoup(content, "lxml")

    def iternodes(self) -> Iterable[Tag]:
        for obj in self.xml.findAll("node"):
            yield obj
