#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import configparser
import pathlib

ME = pathlib.Path(__file__)
BASE = pathlib.Path(__file__).resolve().parent.parent
README = BASE.joinpath("README.md")
CFG = BASE.joinpath("setup.cfg")

keymap = {
    "github-stars": "stargazers",
    "github-forks": "network/members",
    "github-issues": "issues",
}


def badges(github, pkgname):
    urls = [
        f"https://img.shields.io/github/stars/{github}",
        f"https://img.shields.io/github/forks/{github}",
        f"https://img.shields.io/github/issues/{github}",
        f"https://img.shields.io/pypi/v/{pkgname}",
        f"https://img.shields.io/pypi/l/{pkgname}",
        f"https://img.shields.io/pypi/status/{pkgname}",
        f"https://img.shields.io/pypi/dm/{pkgname}",
        f"https://img.shields.io/pypi/pyversions/{pkgname}",
        f"https://img.shields.io/pypi/implementation/{pkgname}",
    ]
    for i in urls:
        arr = i.split("/")
        key = "-".join(arr[3:5])
        if "github" in key:
            if key in keymap:
                url = f"https://github.com/{github}/{keymap[key]}"
            else:
                url = f"https://github.com/{github}"
        elif "pypi" in key:
            url = f"https://pypi.org/project/{pkgname}"
        else:
            raise RuntimeError(f"Unkown key: {key}")
        md = f'[![{key}]({i} "{key}")]({url}) '
        yield md


def get_badges():
    config = configparser.ConfigParser()
    config.read(CFG)
    pkgname = config.get("metadata", "name").replace("_", "-")
    github = "/".join(pathlib.Path(config.get("metadata", "url")).parts[-2:])
    content = "".join(badges(github, pkgname))
    return content


def main():
    """Run main function."""
    content = get_badges()
    with README.open("r+") as fileh:
        data = fileh.read()
        fileh.seek(0)
        data = content + "\n\n" + data
        fileh.write(data)
        fileh.flush()


if __name__ == "__main__":
    main()
