# python-paginate
Pagination support for python web frameworks (study from will_paginate).
It requires Python2.6+ as string.format syntax.

Supported CSS: `bootstrap2&3&4`, `foundation`, `semanticui`, `ink` and `uikit`

Supported web frameworks: Flask, Tornado and Sanic

```
Notice:
Only SemanticUI is tested as I'm using it, please submit PR if has bugs.
```

## Installation

`pip install python-paginate`


If you want to show page info like this:
![page-info](/example/page-info.png "page-info")
above the pagination links,
please add below lines to your css file:

```css

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
```

## Usage

see examples and source code for details.

Run example:

    $cd example
    $virtualenv venv
    $. venv/bin/activate
    $pip install -r requirements.txt
    $python sql.py --help
    $python sql.py init_db
    $python sql.py fill_data --total=307
    $python myapp.py

Open <http://localhost:8000> to see the example page.

![example](/example/example.png "example")
