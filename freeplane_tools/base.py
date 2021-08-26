#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Base class."""
from bs4 import Tag, BeautifulSoup
from freeplane_tools.mm import Mindmap
import re

FLAG_LIST = "child:list"
IMG_EXTS = [
    ".jpg",
    ".png",
    ".svg",
]


class BaseNode(object):
    """Base Node Class."""

    def __init__(self, tag: Tag):
        self.tag = tag
        self.text = tag.attrs.get("text")
        self.link = tag.attrs.get("link")
        self.depth = len(tag.findParents("node"))

    @property
    def note(self):
        note = self.tag.find("richcontent", recursive=False)
        if not note:
            return ""
        lines = []
        for i in note.findAll("p"):
            txt = i.getText().strip("\n").rstrip()
            txt = txt.replace("```", "\n```\n")
            txt = re.sub("^      ", "", txt)
            lines.append(txt)
        retval = "\n".join(lines)
        return retval

    @property
    def list_depth(self):
        for parent in self.tag.findParents("node"):
            t = self.__class__(parent)
            if FLAG_LIST in t.flags:
                return self.depth - t.depth - 1
        return -1

    @property
    def flags(self):
        val = self.tag.findChildren("attribute", recursive=False)
        for i in val:
            yield ":".join(i.attrs.values())

    def list_format(self):
        pad = " " * 3 * self.list_depth
        out = " ".join(i for i in self.text.split("\n"))
        if self.link and self.has_img_link:
            out = " ".join(
                [
                    self.text,
                    self.img_link(self.text),
                ]
            )
        elif self.link:
            out = f"[{self.text}]({self.link})"
        return f"{pad}* {out}"

    def img_link(self, desc=None):
        if not desc:
            return f"![{self.link}]({self.link})"
        return f'![{self.link}]({self.link} "{desc}")'

    @property
    def has_img_link(self):
        if self.link:
            return any(self.link.lower().endswith(i) for i in IMG_EXTS)
        return False

    @property
    def _toc_name(self):
        raise RuntimeError(f"Child class is missing _toc_name method")

    @property
    def toc_entry(self):
        if self.list_depth != -1:
            return ""
        pad = " " * 3 * (self.depth) + "* "
        return f"{pad}[{self.text}](#{self._toc_name})"

    def format(self):
        raise RuntimeError(f"Child class is missing format method")


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
