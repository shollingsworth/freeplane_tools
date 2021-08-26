#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Version bumper on upload."""
import pathlib
import subprocess
from datetime import datetime

BASE = pathlib.Path(__file__).resolve().parent.parent
VFILE = BASE.joinpath("VERSION")
DESTFILE = BASE.joinpath("CHANGLOG.md")

DTFMT = "%Y-%m-%d %H:%M UTC"


def commits(start, end):
    cmd = f"git rev-list {start}...{end}".split()
    return subprocess.check_output(cmd, encoding="utf-8").splitlines()


def commit_details(commit):
    cmd = ["git", "show", "--quiet", commit, "--pretty=%ct:::%s:::%b"]
    epoch, msg, desc = subprocess.check_output(cmd, encoding="utf-8").split(":::")
    dto = datetime.utcfromtimestamp(int(epoch))
    return dto.strftime(DTFMT), msg.strip(), desc.strip()


def main():
    """Run main function."""
    cmd = "git rev-list --max-parents=0 HEAD".split()
    initial_commit = subprocess.check_output(cmd, encoding="utf-8").strip()
    tags = subprocess.check_output(
        ["git", "tag", "-l"],
        encoding="utf-8",
    ).splitlines()[::-1]

    tags.insert(0, "HEAD")
    content = []
    for i in range(len(tags)):
        try:
            end, start = tags[i], tags[i + 1]
        except IndexError:
            end, start = tags[i], initial_commit

        endtxt = end
        subcom = None
        if end == "HEAD":
            endtxt = "Latest"
            subcom = VFILE.read_text()
        content.append(f"# {endtxt}")
        for com in commits(start, end):
            dt, msg, desc = commit_details(com)
            com = subcom or com
            content.append(f"#### {msg}")
            content.append(f"> {dt} {com}")
            content.append("")
            if desc:
                content.append(f"```")
                content.append(desc)
                content.append(f"```")
        content.append("---")
    out = "\n".join(content)
    # print(out)
    with open(DESTFILE, "w") as fileh:
        fileh.write(out)


if __name__ == "__main__":
    main()
