#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mindmap to Bitbucket Markdown."""
from freeplane_tools.base import BaseNode, MindMapInterface
import re


class BitBucketNode(BaseNode):
    """Bitbucket Node class."""

    @property
    def _toc_name(self):
        plc = re.sub("[^a-zA-Z0-9 ]", "", self.text).lower().split()
        plc = "-".join(plc)
        return plc

    def format(self):
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
        lines.append(f'<a name="{self._toc_name}"></a>')
        lines.append(title)
        lines.append(self.note)
        if img_link:
            lines.append(img_link)
        return "\n".join(lines)


class MindMap2StashMarkup(MindMapInterface):
    node = BitBucketNode

    def get_document(self):
        txt = "\n".join(
            [
                '<a name="toc"></a>',
                "# TOC",
                self._toc(),
                "",
                "",
                self._body(),
                "",
            ]
        )
        return txt
