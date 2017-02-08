#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from python_paginate.css import basecss


class Semantic(basecss.BaseCSS):
    _head = '<div class="ui pagination menu{size}{align}{extra}">'
    _normal = '<a class="item" href="{href}">{label}</a>'
    _actived = '<a class="active item">{label}</a>'
    _gap = '<div class="disabled item">{gap}</div>'
    _prev_label = '<i class="left arrow icon"></i>'
    _next_label = '<i class="right arrow icon"></i>'
    _prev_disabled = '<div class="disabled icon item">{label}</div>'
    _next_disabled = '<div class="disabled icon item">{label}</div>'
    _prev_normal = '<a class="icon item" href="{href}">{label}</a>'
    _next_normal = '<a class="icon item" href="{href}">{label}</a>'

    def __init__(self, **kwargs):
        super(Semantic, self).__init__(**kwargs)
