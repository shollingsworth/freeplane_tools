#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test run of script."""
import os
from freeplane_tools.github import MindMap2GithubMarkdown

DIR = os.path.dirname(os.path.abspath(__file__))
TESTFILE = os.path.join(DIR, "template.mm")


def test_bitbucket():
    dfile = os.path.join(DIR, "template.md")
    mm = MindMap2GithubMarkdown(TESTFILE)
    mm.write_document(dfile)


def main():
    """Run main function."""
    test_bitbucket()


if __name__ == "__main__":
    main()
