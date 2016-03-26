#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import basecss


class SemanticUI(basecss.BaseCSS):
    css_head_fmt = '<div class="ui pagination menu{size}{align}{extra}">'
    normal_fmt = '<a class="item" href="{href}">{label}</a>'
    actived_fmt = '<a class="active item">{label}</a>'
    gap_fmt = '<div class="disabled item">{gap}</div>'
    css_prev_label = '<i class="left arrow icon"></i>'
    css_next_label = '<i class="right arrow icon"></i>'
    prev_disabled_fmt = '<div class="disabled icon item">{label}</div>'
    next_disabled_fmt = '<div class="disabled icon item">{label}</div>'
    prev_normal_fmt = '<a class="icon item" href="{href}">{label}</a>'
    next_normal_fmt = '<a class="icon item" href="{href}">{label}</a>'

    def __init__(self, *args, **kwargs):
        super(SemanticUI, self).__init__(*args, **kwargs)
