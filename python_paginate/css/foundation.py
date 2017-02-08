#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from python_paginate.css import basecss


class Foundation(basecss.BaseCSS):
    _align_prefix = ' text-'
    _head = '<ul class="pagination{size}{align}{extra}" \
    role="navigation" aria-label="Pagination">'
    _end = '</ul>'

    _normal = '<li><a href="{href}" aria-label="Page {label}">{label}</a></li>'
    _actived = '<li class="current">\
    <span class="show-for-sr">Current</span> {label}</li>'

    _gap = ' <li class="ellipsis" aria-hidden="true"></li>'

    _prev_disabled = '<li class="pagination-previous disabled">{label} \
    <span class="show-for-sr">page</span></li>'

    _next_disabled = '<li class="pagination-next disabled">{label} \
    <span class="show-for-sr">page</span></li>'

    _prev_normal = '<li class="pagination-previous">\
    <a href="{href}" aria-label="Previous">{label} \
    <span class="show-for-sr">page</span></a></li>'

    _next_normal = '<li class="pagination-next">\
    <a href="{href}" aria-label="Next">{label} \
    <span class="show-for-sr">page</span></a></li>'

    def __init__(self, **kwargs):
        super(Foundation, self).__init__(**kwargs)
