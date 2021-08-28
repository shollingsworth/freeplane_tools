#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mindmap Interface."""
from typing import Iterable
from bs4 import Tag, BeautifulSoup


class Mindmap(object):
    """Mindmap File Interface."""

    def __init__(self, srcfile):
        """Initialize Mindmap."""
        with open(srcfile) as fileh:
            content = fileh.read()
        self.xml = BeautifulSoup(content, "lxml")  # type: BeautifulSoup
        """BeautifulSoup xml iterator."""

    def iternodes(self) -> Iterable[Tag]:
        """Iterate through mindmap nodes."""
        for obj in self.xml.findAll("node"):  # type: ResultSet
            yield obj
