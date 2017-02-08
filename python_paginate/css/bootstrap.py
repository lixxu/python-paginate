#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from python_paginate.css import basecss


class BaseBootstrap(basecss.BaseCSS):
    _size_prefix = ' pagination-'
    _align_prefix = ' pagination-'
    _normal = '<li><a href="{href}">{label}</a></li>'
    _prev_normal = '<li><a href="{href}">{label}</a></li>'
    _next_normal = '<li><a href="{href}">{label}</a></li>'

    def __init__(self, **kwargs):
        super(BaseBootstrap, self).__init__(**kwargs)


class Bootstrap2(BaseBootstrap):
    _head = '<div class="pagination{size}{align}{extra}"><ul>'
    _end = '</ul></div>'
    _actived = '<li class="active"><span>{label}</span></li>'
    _gap = '<li class="disabled"><span>{gap}</span></li>'
    _prev_disabled = '<li class="disabled"><span>{label}</span></li>'
    _next_disabled = '<li class="disabled"><span>{label}</span></li>'

    def __init__(self, **kwargs):
        super(Bootstrap2, self).__init__(**kwargs)


class Bootstrap3(BaseBootstrap):
    _head = '<nav><ul class="pagination{size}{align}{extra}">'
    _end = '</ul></nav>'
    _actived = '<li class="active"><span>{label} <span class="sr-only">\
    (current)</span></span></li>'
    _gap = '<li class="disabled"><span>\
    <span aria-hidden="true">{gap}</span></span></li>'
    _prev_disabled = '<li class="disabled"><span>\
    <span aria-hidden="true">{label}</span></span></li>'
    _next_disabled = '<li class="disabled"><span>\
    <span aria-hidden="true">{label}</span></span></li>'

    def __init__(self, **kwargs):
        super(Bootstrap3, self).__init__(**kwargs)


class Bootstrap4(Bootstrap3):
    _normal = '<li class="page-item">\
    <a class="page-link" href="{href}">{label}</a></li>'

    _actived = '<li class="page-item active"><span class="page-link">{label} \
    <span class="sr-only">(current)</span></span></li>'

    _gap = '<li class="page-item disabled"><span class="page-link">{gap}\
    </span></li>'

    _prev_disabled = '<li class="page-item disabled">\
    <span class="page-link" aria-label="Previous">\
    <span aria-hidden="true">{label}</span>\
    <span class="sr-only">Previous</span></span></li>'

    _next_disabled = '<li class="page-item disabled">\
    <span class="page-link" aria-label="Next">\
    <span aria-hidden="true">{label}</span>\
    <span class="sr-only">Next</span></span></li>'

    _prev_normal = '<li class="page-item">\
    <a class="page-link" href="{href}" aria-label="Previous">\
    <span aria-hidden="true">{label}</span>\
    <span class="sr-only">Previous</span></a></li>'

    _next_normal = '<li class="page-item">\
    <a class="page-link" href="{href}" aria-label="Next">\
    <span aria-hidden="true">{label}</span>\
    <span class="sr-only">Next</span></a></li>'

    def __init__(self, **kwargs):
        super(Bootstrap4, self).__init__(**kwargs)
