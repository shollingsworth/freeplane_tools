#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Convert a Freeplane Mindmap to Github Markdown."""
from freeplane_tools.github import MindMap2GithubMarkdown
import argparse
import re


def main(args):
    """Run main function."""
    mm = MindMap2GithubMarkdown(args.mindmap_file)
    if args.write:
        outfile = args.outfile or re.sub(r".mm$", ".md", args.mindmap_file)
        if args.mindmap_file == outfile:
            raise SystemExit(f"Error, {outfile} is the same as {args.mindmap_file}")
        print(f"Saving file to: {outfile}")
        mm.write_document(outfile)
    else:
        print(mm.get_document(), flush=True)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "mindmap_file",
        help="mindmap_file help",
        type=str,
    )
    parser.add_argument(
        "-w",
        "--write",
        action="store_true",
        help="write markdown file",
        default=False,
    )
    parser.add_argument(
        "-o",
        "--outfile",
        type=str,
        required=False,
        default=None,
    )
    args = parser.parse_args()
    if not re.match(r".*\.mm$", args.mindmap_file):
        raise SystemExit("Invalid file, needs to be a mindmap file")
    # args = parser.parse_args(["./README.mm", "-w"])
    main(args)
