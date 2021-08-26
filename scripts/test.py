#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testing README work."""
from freeplane_tools.github import MindMap2GithubMarkdown
import pathlib
import subprocess

BASE = pathlib.Path(__file__).parent.parent


def main():
    """Run main function."""
    mm = MindMap2GithubMarkdown(BASE.joinpath("README.mm"))
    mm.write_document(BASE.joinpath("README.md"))
    subprocess.check_output([BASE.joinpath("scripts", "gencli.py")])


if __name__ == "__main__":
    main()
