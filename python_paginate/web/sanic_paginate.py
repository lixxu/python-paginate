#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
try:
    from jinja2 import Markup
except ImportError:
    def Markup(text):
        return text

from python_paginate.web import base_paginate


class Pagination(base_paginate.BasePagination):
    def __init__(self, request=None, **kwargs):
        if not request and 'url' not in kwargs:
            raise ValueError('request or url is required')

        kwargs.setdefault('page_name', self._page_name)
        kwargs.setdefault('per_page_name', self._per_page_name)
        if request:
            kwargs.setdefault('url', request.url)
            page_name = kwargs['page_name']
            per_page_name = kwargs['per_page_name']
            page, per_page, skip = self.get_page_args(request, page_name,
                                                      per_page_name)
            kwargs.setdefault(page_name, page)
            kwargs.setdefault(per_page_name, per_page)

        super(Pagination, self).__init__(**kwargs)

    @staticmethod
    def get_page_args(request, page_name=None, per_page_name=None):
        page = request.args.get(page_name or Pagination._page_name, 1)
        per_page = request.args.get(per_page_name or Pagination._per_page_name,
                                    10)
        try:
            per_page = int(per_page)
        except:
            per_page = 10

        try:
            page = int(page)
        except:
            page = 1

        return page, per_page, per_page * (page - 1)

    @property
    def single_link(self):
        return Markup(self.raw_single_link)

    @property
    def links(self):
        return Markup(self.raw_links)

    @property
    def info(self):
        return Markup(self.raw_info)
