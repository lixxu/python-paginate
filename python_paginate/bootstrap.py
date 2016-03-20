#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import basecss


class BaseBootstrapCSS(basecss.BaseCSS):
    normal_fmt = '<li><a href="{href}">{label}</a></li>'
    prev_normal_fmt = '<li><a href="{href}">{label}</a></li>'
    next_normal_fmt = '<li><a href="{href}">{label}</a></li>'

    def __init__(self, *args, **kwargs):
        super(BaseBootstrapCSS, self).__init__(*args, **kwargs)

    def get_adjust_size(self, size):
        return ' pagination-' + size if size else ''

    def get_adjust_align(self, align):
        return ' pagination-' + align if align else ''


class Bootstrap2CSS(BaseBootstrapCSS):
    css_head_fmt = '<div class="pagination{size}{align}"><ul>'
    css_end_fmt = '</ul></div>'
    actived_fmt = '<li class="active"><span>{label}</span></li>'
    gap_fmt = '<li class="disabled"><span>{gap}</span></li>'
    prev_disabled_fmt = '<li class="disabled"><span>{label}</span></li>'
    next_disabled_fmt = '<li class="disabled"><span>{label}</span></li>'

    def __init__(self, *args, **kwargs):
        super(Bootstrap2CSS, self).__init__(*args, **kwargs)


class Bootstrap3CSS(BaseBootstrapCSS):
    css_head_fmt = '<nav><ul class="pagination{size}{align}">'
    css_end_fmt = '</ul></nav>'
    actived_fmt = '<li class="active"><span>{label} <span class="sr-only">\
    (current)</span></span></li>'
    gap_fmt = '<li class="disabled"><span>\
    <span aria-hidden="true">{gap}</span></span></li>'
    prev_disabled_fmt = '<li class="disabled"><span>\
    <span aria-hidden="true">{label}</span></span></li>'
    next_disabled_fmt = '<li class="disabled"><span>\
    <span aria-hidden="true">{label}</span></span></li>'

    def __init__(self, *args, **kwargs):
        super(Bootstrap3CSS, self).__init__(*args, **kwargs)


class Bootstrap4CSS(Bootstrap3CSS):
    normal_fmt = '<li class="page-item">\
    <a class="page-link" href="{href}">{label}</a></li>'

    actived_fmt = '<li class="page-item active">\
    <span class="page-link">{label} <span class="sr-only">(current)</span>\
    </span></li>'

    gap_fmt = '<li class="page-item disabled">\
    <span class="page-link">{gap}</span></li>'

    prev_disabled_fmt = '<li class="page-item disabled">\
    <span class="page-link" aria-label="Previous">\
    <span aria-hidden="true">{label}</span>\
    <span class="sr-only">Previous</span></span></li>'

    next_disabled_fmt = '<li class="page-item disabled">\
    <span class="page-link" aria-label="Next">\
    <span aria-hidden="true">{label}</span>\
    <span class="sr-only">Next</span></span></li>'

    prev_normal_fmt = '<li class="page-item">\
    <a class="page-link" href="{href}" aria-label="Previous">\
    <span aria-hidden="true">{label}</span>\
    <span class="sr-only">Previous</span></a></li>'

    next_normal_fmt = '<li class="page-item">\
    <a class="page-link" href="{href}" aria-label="Next">\
    <span aria-hidden="true">{label}</span>\
    <span class="sr-only">Next</span></a></li>'

    def __init__(self, *args, **kwargs):
        super(Bootstrap3CSS, self).__init__(*args, **kwargs)
