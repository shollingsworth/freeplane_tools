#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mindmap to Markdown."""
from bs4 import BeautifulSoup, Tag
import re

FLAG_LIST = "child:list"


class Node(object):
    """Node Class."""

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
            t = Node(parent)
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
        out = self.text
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
        img_exts = [
            ".jpg",
            ".png",
            ".svg",
        ]
        if self.link:
            return any(self.link.lower().endswith(i) for i in img_exts)
        return False

    @property
    def _toc_name(self):
        plc = re.sub("[^a-zA-Z0-9 ]", "", self.text).lower().split()
        plc = "-".join(plc)
        return plc

    @property
    def toc_entry(self):
        if self.list_depth != -1:
            return ""
        pad = " " * 3 * (self.depth) + "* "
        return f"{pad}[{self.text}](#{self._toc_name})"

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


class MindMap2StashMarkup(object):
    def __init__(self, srcfile):
        with open(srcfile) as fileh:
            content = fileh.read()
        self.content = content
        self.xml = BeautifulSoup(content, "lxml")

    def _iternodes(self):
        for obj in self.xml.findAll("node"):
            yield Node(obj)

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
