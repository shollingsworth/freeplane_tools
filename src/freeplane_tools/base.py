#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Base class."""
from bs4 import Tag
from freeplane_tools.mm import Mindmap
import re

FLAG_LIST = "child:list"
"""Flag for sub nodes being list elements of different depths."""

IMG_EXTS = [
    ".jpg",
    ".png",
    ".svg",
]
"""Image extensions that will embed images instead of linking to them."""


class BaseNode(object):
    """Base Node Class."""

    def __init__(self, tag: Tag):  # type: bs4.Tag
        """Initialize Node Class."""
        self.tag = tag
        """Beautiful Soup Tag."""
        self.text = tag.attrs.get("text")
        """Node Text."""
        self.link = tag.attrs.get("link")
        """Node text (if it exists)."""
        self.depth = len(tag.findParents("node"))
        """Node depth in hierachy of Mindmap."""

    @property
    def note(self):
        """Node "note" Property

        This iterates through the html inside the note and strips the start
        padding
        """
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
        """Return integer representing the depth of the node in the mindmap tree."""
        for parent in self.tag.findParents("node"):
            t = self.__class__(parent)
            if FLAG_LIST in t.flags:
                return self.depth - t.depth - 1
        return -1

    @property
    def flags(self):
        """Custom attribute flags for the node (see FLAG_*)."""
        val = self.tag.findChildren("attribute", recursive=False)
        for i in val:
            yield ":".join(i.attrs.values())

    def list_format(self):
        """How to format list elements when parents have the FLAG_LIST attribute set."""
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
        """Return a link that has IMG_EXTS in the link text."""
        if not desc:
            return f"![{self.link}]({self.link})"
        return f'![{self.link}]({self.link} "{desc}")'

    @property
    def has_img_link(self):
        """Return true if a node link ends in a value from IMG_EXTS."""
        if self.link:
            return any(self.link.lower().endswith(i) for i in IMG_EXTS)
        return False

    @property
    def _toc_name(self):
        """Abstract table of contents name."""
        raise RuntimeError(f"Child class is missing _toc_name method")

    @property
    def toc_entry(self):
        """Return the nodes TOC entry."""
        if self.list_depth != -1:
            return ""
        pad = " " * 3 * (self.depth) + "* "
        return f"{pad}[{self.text}](#{self._toc_name})"

    def format(self):
        """Abstract for the node format."""
        raise RuntimeError(f"Child class is missing format method")


class MindMapInterface(object):
    """Base class for Mindmaps."""

    # Needs to be defined in subclass
    node = None  # type:BaseNode
    """Abstract node type (subclass of BaseNode)."""

    def __init__(self, srcfile: str):
        """Initialize MindMapInterface with src file."""
        self.mm = Mindmap(srcfile)  # type: Mindmap
        """Mindmap class."""
        if self.__class__.node is None:
            raise RuntimeError(f"Please define {__class__}.node")

    def _iternodes(self):
        """Iterate through ."""
        for obj in self.mm.iternodes():
            yield self.__class__.node(obj)

    def _toc(self):
        """Toc values for mindmap."""
        return "\n".join(n.toc_entry for n in self._iternodes() if n.toc_entry)

    def _body(self):
        """Main Body for Mindmap."""
        return "\n".join(n.format() for n in self._iternodes())

    def get_document(self):
        """Return assembled Document."""
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

    def write_document(self, dstfile: str):
        """Write assembled document to file."""
        with open(dstfile, "w") as fileh:
            fileh.write(self.get_document())
