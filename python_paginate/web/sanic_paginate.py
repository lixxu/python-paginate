#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from python_paginate.web import base_paginate


def get_page_args(request, page_name='page', per_page_name='per_page'):
    per_page = request.args.get(per_page_name, 10)
    page = request.args.get(page_name, 1)
    try:
        per_page = int(per_page)
    except:
        per_page = 10

    try:
        page = int(page)
    except:
        page = 1

    return page, per_page


class SanicPagination(base_paginate.BasePagination):
    def __init__(self, request=None, **kwargs):
        if not request and 'url' not in kwargs:
            raise ValueError('request or url is required')

        kwargs.setdefault('page_name', 'page')
        kwargs.setdefault('per_page_name', 'per_page')
        if request:
            kwargs.setdefault('url', request.url)
            page_name = kwargs['page_name']
            per_page_name = kwargs['per_page_name']
            page, per_page = get_page_args(request, page_name, per_page_name)
            kwargs.setdefault(page_name, page)
            kwargs.setdefault(per_page_name, per_page)

        super(SanicPagination, self).__init__(**kwargs)
