#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from python_paginate.web import base_paginate


class Pagination(base_paginate.BasePagination):
    def __init__(self, **kwargs):
        if 'url' not in kwargs:
            raise ValueError('request url is required')

        super(Pagination, self).__init__(**kwargs)

    @staticmethod
    def get_page_args(handler, page_name=None, per_page_name=None):
        page = handler.get_argument(page_name or Pagination._page_name, 1)
        pp_name = per_page_name or Pagination._per_page_name
        per_page = handler.get_argument(pp_name, 10)
        try:
            per_page = int(per_page)
        except:
            per_page = 10

        try:
            page = int(page)
        except:
            page = 1

        return page, per_page, per_page * (page - 1)
