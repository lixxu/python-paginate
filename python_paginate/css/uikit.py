#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import basecss


class UIKit(basecss.BaseCSS):
    css_head_fmt = '<ul class="uk-pagination{size}{align}{extra}">'
    css_end_fmt = '</ul>'

    normal_fmt = '<li><a href="{href}">{label}</a></li>'
    actived_fmt = '<li class="uk-active"><span>{label}</span></li>'

    gap_fmt = '<li class="uk-disabled"><span>{gap}</span></li>'

    prev_disabled_fmt = '<li class="uk-disabled"><span>{label}</span></li>'

    next_disabled_fmt = '<li class="uk-disabled"><span>{label}</span></li>'

    prev_normal_fmt = '<li class="uk-pagination-previous">\
    <a href="{href}">{label}</a></li>'

    next_normal_fmt = '<li class="uk-pagination-next">\
    <a href="{href}">{label}</a></li>'

    def __init__(self, *args, **kwargs):
        super(UIKit, self).__init__(*args, **kwargs)

    def get_adjust_align(self, align):
        return ' uk-pagination-' + align if align else ''
