#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys
from flask import request, url_for, Markup, current_app
from python_paginate.web import base_paginate

PY2 = sys.version_info[0] == 2


class Pagination(base_paginate.BasePagination):
    def __init__(self, *args, **kwargs):
        self.flask_init()
        super(Pagination, self).__init__(**kwargs)

    @classmethod
    def get_page_args(page_name=None, per_page_name=None):
        pp_name = per_page_name or Pagination._per_page_name

        args = request.args.copy()
        args.update(request.view_args.copy())
        page = int(args.get(page_name or Pagination._page_name, 1))
        per_page = args.get(pp_name)
        if per_page:
            per_page = int(per_page)
        else:
            per_page = current_app.config.get(pp_name.upper(), 10)

        return page, per_page, per_page * (page - 1)

    def flask_init(self):
        self.endpoint = request.endpoint
        args = request.args.copy()
        args.update(request.view_args.copy())
        self.url_args = {}
        for k, v in args.lists():
            if len(v) == 1:
                self.url_args[k] = v[0]
            else:
                self.url_args[k] = v

    def get_href(self, page):
        if self.href:
            url = self.href.format(page or 1)
        else:
            self.url_args[self.page_name] = page
            url = url_for(self.endpoint, **self.url_args)

        # Need to return a unicode object
        return url.decode('utf8') if PY2 else url

    @property
    def single_link(self):
        return Markup(self.raw_single_link)

    @property
    def links(self):
        return Markup(self.raw_links)

    @property
    def info(self):
        return Markup(self.raw_info)
