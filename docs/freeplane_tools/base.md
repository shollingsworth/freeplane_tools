Module freeplane_tools.base
===========================
Base class.

Classes
-------

`BaseNode(tag: bs4.element.Tag)`
:   Base Node Class.

    ### Descendants

    * freeplane_tools.bitbucket.BitBucketNode
    * freeplane_tools.github.GithubNode

    ### Instance variables

    `flags`
    :

    `has_img_link`
    :

    `list_depth`
    :

    `note`
    :

    `toc_entry`
    :

    ### Methods

    `format(self)`
    :

    `img_link(self, desc=None)`
    :

    `list_format(self)`
    :

`MindMapInterface(srcfile)`
:   

    ### Descendants

    * freeplane_tools.bitbucket.MindMap2StashMarkup

    ### Class variables

    `node`
    :

    ### Methods

    `get_document(self)`
    :

    `write_document(self, dstfile)`
    :