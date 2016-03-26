#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import basecss


class Foundation(basecss.BaseCSS):
    css_head_fmt = '<ul class="pagination{size}{align}{extra}" \
    role="navigation" aria-label="Pagination">'
    css_end_fmt = '</ul>'

    normal_fmt = '<li><a href="{href}" aria-label="Page {label}">{label}</a>\
    </li>'
    actived_fmt = '<li class="current">\
    <span class="show-for-sr">Current</span> {label}</li>'

    gap_fmt = ' <li class="ellipsis" aria-hidden="true"></li>'

    prev_disabled_fmt = '<li class="pagination-previous disabled">{label} \
    <span class="show-for-sr">page</span></li>'

    next_disabled_fmt = '<li class="pagination-next disabled">{label} \
    <span class="show-for-sr">page</span></li>'

    prev_normal_fmt = '<li class="pagination-previous">\
    <a href="{href}" aria-label="Previous">{label} \
    <span class="show-for-sr">page</span></a></li>'

    next_normal_fmt = '<li class="pagination-next">\
    <a href="{href}" aria-label="Next">{label} \
    <span class="show-for-sr">page</span></a></li>'

    def __init__(self, *args, **kwargs):
        super(Foundation, self).__init__(*args, **kwargs)

    def get_adjust_align(self, align):
        return ' text-' + align if align else ''
