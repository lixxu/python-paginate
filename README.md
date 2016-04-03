python-paginate
==============

Pagination support for python web frameworks (study from will_paginate).
It requires Python2.6+ as string.format syntax.

Supported CSS: `bootstrap2&3&4`, `foundation`, `semanticui`, `ink` and `uikit`

Supported web frameworks: Flask, Tornado

Notice:
Only `SemanticUI` is tested as I'm using it.

If you want to show pagination-info
("Total <b>100</b> posts, displaying <b>20 - 30</b>")
above the pagination links,
please add below lines to your css file::

.. sourcecode:: css

    .pagination-page-info {
        padding: .6em;
        padding-left: 0;
        width: 40em;
        margin: .5em;
        margin-left: 0;
        font-size: 12px;
    }
    .pagination-page-info b {
        color: black;
        background: #6aa6ed;
        padding-left: 2px;
        padding: .1em .25em;
        font-size: 150%;
    }

