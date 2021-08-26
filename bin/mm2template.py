#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Copy a Mindmap Template to destination file."""
from freeplane_tools.data import get_template
import argparse
import re


def main(args):
    """Run main function."""
    if not re.match(r".*\.mm$", args.dest_file):
        raise SystemExit(f"Destination file needs to end with .mm")
    content = get_template()
    with open(args.dest_file, "wb") as fileh:
        print(f"Writing to file: {args.dest_file}")
        fileh.write(content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "dest_file",
        help="destination file",
        type=str,
    )
    args = parser.parse_args()
    # args = parser.parse_args(["./test.mm"])
    main(args)
