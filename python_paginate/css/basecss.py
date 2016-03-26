#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals


class BaseCSS(object):
    css_head_fmt = '<div class="pagination{size}{align}{extra}">'
    css_end_fmt = '</div>'
    normal_fmt = '<a class="item" href="{href}">{label}</a>'
    actived_fmt = '<a class="active">{label}</a>'
    gap_fmt = '<div class="disabled">{gap}</div>'
    css_prev_label = '&laquo;'
    css_next_label = '&raquo;'
    prev_disabled_fmt = '<div class="disabled">{label}</div>'
    next_disabled_fmt = '<div class="disabled">{label}</div>'
    prev_normal_fmt = '<a class="item" href="{href}">{label}</a>'
    next_normal_fmt = '<a class="item" href="{href}">{label}</a>'

    def __init__(self, *args, **kwargs):
        self.size = self.get_adjust_size(kwargs.get('size') or '')
        self.align = self.get_adjust_align(kwargs.get('align') or '')
        self.extra = self.get_adjust_extra(kwargs.get('extra') or '')
        self.prev_label = kwargs.get('prev_label') or self.css_prev_label
        self.next_label = kwargs.get('next_label') or self.css_next_label
        self.gap_marker = kwargs.get('gap_marker') or '...'

    @property
    def css_head(self):
        return self.css_head_fmt.format(size=self.size, align=self.align,
                                        extra=self.extra)

    def get_adjust_size(self, size=''):
        return ' ' + size if size else ''

    def get_adjust_align(self, align=''):
        return ' ' + align if align else ''

    def get_adjust_extra(self, extra=''):
        return ' ' + extra if extra else ''

    @property
    def css_end(self):
        return self.css_end_fmt

    def get_normal(self, href='', label=''):
        return self.normal_fmt.format(href=href, label=label)

    def get_actived(self, href='', label=''):
        return self.actived_fmt.format(href=href, label=label)

    @property
    def gap(self):
        return self.gap_fmt.format(gap=self.gap_marker)

    def get_side(self, href='#', disabled=False, side='prev'):
        if disabled:
            fmt = getattr(self, side + '_disabled_fmt')
        else:
            fmt = getattr(self, side + '_normal_fmt')

        return fmt.format(href=href, label=getattr(self, side + '_label'))

    def get_prev(self, href='', disabled=False):
        return self.get_side(href, disabled=disabled, side='prev')

    def get_next(self, href='', disabled=False):
        return self.get_side(href, disabled=disabled, side='next')
