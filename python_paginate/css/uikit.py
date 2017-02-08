#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from python_paginate.css import basecss


class UIKit(basecss.BaseCSS):
    _align_prefix = ' uk-pagination-'
    _head = '<ul class="uk-pagination{size}{align}{extra}">'
    _end = '</ul>'

    _normal = '<li><a href="{href}">{label}</a></li>'
    _actived = '<li class="uk-active"><span>{label}</span></li>'
    _gap = '<li class="uk-disabled"><span>{gap}</span></li>'

    _prev_disabled = '<li class="uk-disabled"><span>{label}</span></li>'
    _next_disabled = '<li class="uk-disabled"><span>{label}</span></li>'

    _prev_normal = '<li class="uk-pagination-previous">\
    <a href="{href}">{label}</a></li>'

    _next_normal = '<li class="uk-pagination-next">\
    <a href="{href}">{label}</a></li>'

    def __init__(self, **kwargs):
        super(UIKit, self).__init__(**kwargs)
