#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import base_paginate


def get_page_args(handler):
    per_page = handler.get_argument('per_page', 10)
    page = handler.get_argument('page', 1)
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
