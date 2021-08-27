[![github-stars](https://img.shields.io/github/stars/shollingsworth/freeplane_tools "github-stars")](https://github.com/shollingsworth/freeplane_tools/stargazers) [![github-forks](https://img.shields.io/github/forks/shollingsworth/freeplane_tools "github-forks")](https://github.com/shollingsworth/freeplane_tools/network/members) [![github-issues](https://img.shields.io/github/issues/shollingsworth/freeplane_tools "github-issues")](https://github.com/shollingsworth/freeplane_tools/issues) [![pypi-v](https://img.shields.io/pypi/v/freeplane-tools "pypi-v")](https://pypi.org/project/freeplane-tools) [![pypi-l](https://img.shields.io/pypi/l/freeplane-tools "pypi-l")](https://pypi.org/project/freeplane-tools) [![pypi-status](https://img.shields.io/pypi/status/freeplane-tools "pypi-status")](https://pypi.org/project/freeplane-tools) [![pypi-dm](https://img.shields.io/pypi/dm/freeplane-tools "pypi-dm")](https://pypi.org/project/freeplane-tools) [![pypi-pyversions](https://img.shields.io/pypi/pyversions/freeplane-tools "pypi-pyversions")](https://pypi.org/project/freeplane-tools) [![pypi-implementation](https://img.shields.io/pypi/implementation/freeplane-tools "pypi-implementation")](https://pypi.org/project/freeplane-tools) 

# TOC
* [Freeplane Tools](#freeplane-tools-)
   * [Installation](#installation-)
   * [License](#license-)
   * [Quickstart](#quickstart-)
      * [Example](#example-)
   * [CLI Commands](#cli-commands-)
   * [Building](#building-)
   * [Other Docs](#other-docs-)
      * [API Docs](#api-docs-)
      * [Changelog](#changelog-)


# Freeplane Tools [&#8593;](#toc)
If you hate writing Markdown, but love mindmaps (and using [freeplane](https://www.freeplane.org/wiki/index.php/Home) this toolset is for you.

These python programs aim to ease translating a mindmap into various markdown formats.

This document [README.md](./README.md) was made with `mm2github.py` with  [from README.mm](./README.mm) as a source.

Enjoy!

Pull requests welcome. :)
## Installation [&#8593;](#toc)
To install this package from [pypy](https://pypi.org/project/freeplane-tools/) run the following command.


```

pip3 install freeplane_tools

```

## License [&#8593;](#toc)
See: [LICENSE](./LICENSE)
## Quickstart [&#8593;](#toc)
Run the following if you want a quick demo of how this works. Have `freeplane` installed before running this.


```

pip3 install freeplane_tools

mm2template.py mymindmap.mm

freeplane mymindmap.mm

# do your editing in freeplane

mm2github.py -w mymindmap.mm


```

This will create: `mymindmap.md`
### Example [&#8593;](#toc)
Just want to look?

[This](./examples/template.mm) mindmap produces the following [markdown](./examples/template.md)
## CLI Commands [&#8593;](#toc)
*mm2bitbucket_server.py*
```
usage: mm2bitbucket_server.py [-h] [-w] [-o OUTFILE] mindmap_file

Convert a Freeplane Mindmap to Bitbucket Markdown.

positional arguments:
  mindmap_file          mindmap_file help

optional arguments:
  -h, --help            show this help message and exit
  -w, --write           write markdown file
  -o OUTFILE, --outfile OUTFILE

```
---
*mm2github.py*
```
usage: mm2github.py [-h] [-w] [-o OUTFILE] mindmap_file

Convert a Freeplane Mindmap to Github Markdown.

positional arguments:
  mindmap_file          mindmap_file help

optional arguments:
  -h, --help            show this help message and exit
  -w, --write           write markdown file
  -o OUTFILE, --outfile OUTFILE

```
---
*mm2template.py*
```
usage: mm2template.py [-h] dest_file

Copy a Mindmap Template to destination file.

positional arguments:
  dest_file   destination file

optional arguments:
  -h, --help  show this help message and exit

```
---
## Building [&#8593;](#toc)
os / Package prerequisites:

```

pip3 install twine pdoc3

```

* Install Locally from current branch
   * ``` make install_local ```
* Build Package
   * ``` make pkg ```
* Release
   * ```make documentation```
      * Make sure git tree is clean
   * ```make bump_release```
   * ```make release```
## Other Docs [&#8593;](#toc)

### API Docs [\[link\]](https://shollingsworth.github.io/freeplane_tools/) [&#8593;](#toc)

### Changelog [\[link\]](./CHANGELOG.md) [&#8593;](#toc)

