#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from python_paginate.css import basecss


class Ink(basecss.BaseCSS):
    _head = '<nav class="ink-navigation">\
    <ul class="pagination{size}{align}{extra}">'
    _end = '</ul></nav>'

    _normal = '<li><a href="{href}">{label}</a></li>'
    _actived = '<li class="active"><a href="{href}">{label}</a></li>'
    _gap = '<li class="disabled"><a href="{href}">{gap}</a></li>'

    _prev_disabled = '<li class="disabled"><a href="{href}">{label}</a></li>'
    _next_disabled = '<li class="disabled"><a href="{href}">{label}</a></li>'

    _prev_normal = '<li><a href="{href}">{label}</a></li>'
    _next_normal = '<li><a href="{href}">{label}</a></li>'

    def __init__(self, **kwargs):
        super(Ink, self).__init__(**kwargs)
