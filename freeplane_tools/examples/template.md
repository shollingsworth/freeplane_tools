# TOC
* [Demo Mindmap](#demo-mindmap-)
   * [Heading 1](#heading-1-)
   * [Heading 1 - children are list](#heading-1---children-are-list-)
   * [Heading 1 - plain](#heading-1---plain-)
      * [Heading 2](#heading-2-)
         * [Heading 3](#heading-3-)
         * [Heading 3 - But with children](#heading-3---but-with-children-)
      * [Heading 2 - code snip](#heading-2---code-snip-)


# Demo Mindmap [&#8593;](#toc)

## Heading 1 [&#8593;](#toc)
This is text under the heading

And formatted with standard markdown.

[google](http://www.google.com)
---
## Heading 1 - children are list [&#8593;](#toc)

* Grace Hopper ![grace_hopper.jpg](grace_hopper.jpg "Grace Hopper")
* [This is a url](https://www.google.com)
* Level 1 - foo
   * Level 2 - foo
      * Level 3 - foo
      * Level 3 - bar
      * Level 3 - baz
      * Grace Hopper ![grace_hopper.jpg](grace_hopper.jpg "Grace Hopper")
   * Level 2 - bar
   * Level 2 - baz
* Level 1 - bar
* Level 1 - baz
## Heading 1 - plain [&#8593;](#toc)

### Heading 2 [&#8593;](#toc)
This is heading # 2

This goes directly below the heading
#### Heading 3 [&#8593;](#toc)
This is the context for heading #3
#### Heading 3 - But with children [&#8593;](#toc)

* Level 1 - foo
   * Level 2 - foo
      * Level 3 - foo
      * Level 3 - bar
      * Level 3 - baz
      * Grace Again! ![grace_hopper.jpg](grace_hopper.jpg "Grace Again!")
   * Level 2 - bar
   * Level 2 - baz
* Level 1 - bar
* Level 1 - baz
### Heading 2 - code snip [&#8593;](#toc)
Bash


```

cnt=0
while true; do
   echo "Counting: ${cnt}"
   cnt=$((cnt + 1))
   test ${cnt} -gt 1000 && break
done

```

