Module freeplane_tools.github
=============================
Mindmap to Github Markdown.

Classes
-------

`GithubNode(tag: bs4.element.Tag)`
:   Github Node Class.

    ### Ancestors (in MRO)

    * freeplane_tools.base.BaseNode

    ### Methods

    `format(self)`
    :

`MindMap2GithubMarkdown(srcfile)`
:   

    ### Ancestors (in MRO)

    * freeplane_tools.github.MindMapInterface

    ### Class variables

    `node`
    :   Github Node Class.

    ### Methods

    `get_document(self)`
    :

`MindMapInterface(srcfile)`
:   

    ### Descendants

    * freeplane_tools.github.MindMap2GithubMarkdown

    ### Class variables

    `node`
    :

    ### Methods

    `get_document(self)`
    :

    `write_document(self, dstfile)`
    :