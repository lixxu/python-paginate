#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from python_paginate.css import basecss

NORMAL = (
    '<li class="page-item"><a class="page-link" href="{href}">{label}</a></li>'
)
ACTIVED = '<li class="page-item active"><a class="page-link">{label}</a></li>'
PREV_DISABLED = '<li class="page-item disabled"><a class="page-link" \
tabindex="-1">{label}</a></li>'
NEXT_DISABLED = PREV_DISABLED
NEXT_NORMAL = '<li class="page-item service"><a class="page-link" \
href="{href}">{label}</a></li>'


class Metro4(basecss.BaseCSS):
    _head = '<ul class="pagination {size}{align}{extra}">'
    _end = "</ul>"
    _normal = NORMAL
    _actived = ACTIVED
    _gap = '<li class="page-item no-link"><a class="page-link">{gap}</a></li>'
    _prev_label = '<span class="mif-chevron-thin-left"></span>'
    _next_label = '<span class="mif-chevron-thin-right"></span>'
    _prev_disabled = PREV_DISABLED
    _next_disabled = NEXT_DISABLED
    _prev_normal = NORMAL
    _next_normal = NEXT_NORMAL

    def __init__(self, **kwargs):
        super(Metro4, self).__init__(**kwargs)
