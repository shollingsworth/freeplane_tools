#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mindmap to Github Markdown."""
from freeplane_tools.base import BaseNode, MindMapInterface
from freeplane_tools.mm import Mindmap
import re


class GithubNode(BaseNode):
    """Github Node Class."""

    @property
    def _toc_name(self):
        """Table of contents name for node."""
        return re.sub("[^a-zA-Z0-9]", "-", self.text).lower() + "-"

    def format(self):
        """Formatted output for node."""
        if self.list_depth >= 0:
            return self.list_format()
        lines = []
        title_pad = "#" * (self.depth + 1)
        title = self.text
        img_link = ""
        if self.link and self.has_img_link:
            img_link = self.img_link()
        elif self.link:
            title = f"{self.text} [\[link\]]({self.link})"
        title = f"{title_pad} {title} [&#8593;](#toc)"
        lines.append(title)
        lines.append(self.note)
        if img_link:
            lines.append(img_link)
        return "\n".join(lines)


class MindMap2GithubMarkdown(MindMapInterface):
    """Mindmap / Github Markdown Class."""

    node = GithubNode

    def get_document(self):
        txt = "\n".join(
            [
                "# TOC",
                self._toc(),
                "",
                "",
                self._body(),
                "",
            ]
        )
        return txt
