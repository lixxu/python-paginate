#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os.path
import tempfile
from sanic import Sanic
import sqlite3
from sanic_jinja2 import SanicJinja2
from python_paginate.css.semantic import Semantic
from python_paginate.web.sanic_paginate import Pagination

app = Sanic(__name__)

# update pagination settings
settings = dict(PREV_LABEL='<i class="left chevron icon"></i>',
                NEXT_LABEL='<i class="right chevron icon"></i>',
                PER_PAGE=10,  # default is 10
                DB_PATH=os.path.join(tempfile.gettempdir(), 'test.db'),
                )
app.config.update(settings)

jinja = SanicJinja2(app, autoescape=True)

# customize default pagination
if 'PREV_LABEL' in app.config:
    Semantic._prev_label = app.config.PREV_LABEL

if 'NEXT_LABEL' in app.config:
    Semantic._next_label = app.config.NEXT_LABEL

Pagination._css = Semantic()  # for cache
# or
# Pagination._css_framework = 'semantic'
# like above line, but little different
# if you want to get same result, need do below:
# pass css_prev_label, css_next_label to Pagination for initialize

Pagination._per_page = app.config.PER_PAGE


@app.route('/')
async def index(request):
    conn = sqlite3.connect(app.config.DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('select count(*) from users')
    total = cur.fetchone()[0]
    page, per_page, offset = Pagination.get_page_args(request)
    sql = 'select name from users limit {}, {}'\
        .format(offset, per_page)
    cur.execute(sql)
    users = cur.fetchall()
    cur.close()
    conn.close()
    pagination = Pagination(request, total=total, record_name='users')
    return await jinja.render('index.html', users=users, pagination=pagination,
                              request=request)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
