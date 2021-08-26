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
        return re.sub("[^a-zA-Z0-9]", "-", self.text).lower() + "-"

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
        lines.append(title)
        lines.append(self.note)
        if img_link:
            lines.append(img_link)
        return "\n".join(lines)


class MindMapInterface(object):
    # Needs to be defined in subclass
    node = None

    def __init__(self, srcfile):
        self.mm = Mindmap(srcfile)
        if self.__class__.node is None:
            raise RuntimeError(f"Please define {__class__}.node")

    def _iternodes(self):
        for obj in self.mm.iternodes():
            yield self.__class__.node(obj)

    def _toc(self):
        return "\n".join(n.toc_entry for n in self._iternodes() if n.toc_entry)

    def _body(self):
        return "\n".join(n.format() for n in self._iternodes())

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

    def write_document(self, dstfile):
        with open(dstfile, "w") as fileh:
            fileh.write(self.get_document())


class MindMap2GithubMarkdown(MindMapInterface):
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
