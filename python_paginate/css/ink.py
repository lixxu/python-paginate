#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import basecss


class Ink(basecss.BaseCSS):
    css_head_fmt = '<nav class="ink-navigation">\
    <ul class="pagination{size}{align}{extra}">'
    css_end_fmt = '</ul></nav>'

    normal_fmt = '<li><a href="{href}">{label}</a></li>'

    actived_fmt = '<li class="active"><a href="{href}">{label}</a></li>'
    gap_fmt = '<li class="disabled"><a href="{href}">{gap}</a></li>'

    prev_disabled_fmt = '<li class="disabled">\
    <a href="{href}">{label}</a></li>'
    next_disabled_fmt = '<li class="disabled">\
    <a href="{href}">{label}</a></li>'

    prev_normal_fmt = '<li><a href="{href}">{label}</a></li>'
    next_normal_fmt = '<li><a href="{href}">{label}</a></li>'

    def __init__(self, *args, **kwargs):
        super(Ink, self).__init__(*args, **kwargs)
