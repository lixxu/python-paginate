#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from python_paginate.web import base_paginate


def get_page_args(handler, page_name='page', per_page_name='per_page'):
    per_page = handler.get_argument(per_page_name, 10)
    page = handler.get_argument(page_name, 1)
    try:
        per_page = int(per_page)
    except:
        per_page = 10

    try:
        page = int(page)
    except:
        page = 1

    return page, per_page


class TornadoPagination(base_paginate.BasePagination):
    def __init__(self, **kwargs):
        if 'url' not in kwargs:
            raise ValueError('request url is required')

        super(TornadoPagination, self).__init__(**kwargs)
