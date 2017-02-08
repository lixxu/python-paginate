#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

INIT_KEYS = 'size align extra head end normal actived gap gap_marker \
prev_label next_label prev_disabled next_disabled prev_normal next_normal\
'.split()


class BaseCSS(object):
    _size = ''
    _align = ''
    _extra = ''
    _size_prefix = ' '
    _align_prefix = ' '
    _extra_prefix = ' '
    _head = '<div class="pagination{size}{align}{extra}">'
    _end = '</div>'
    _normal = '<a class="item" href="{href}">{label}</a>'
    _actived = '<a class="active">{label}</a>'
    _gap = '<div class="disabled">{gap}</div>'
    _gap_marker = '...'
    _prev_label = '&laquo;'
    _next_label = '&raquo;'
    _prev_disabled = '<div class="disabled">{label}</div>'
    _next_disabled = '<div class="disabled">{label}</div>'
    _prev_normal = '<a class="item" href="{href}">{label}</a>'
    _next_normal = '<a class="item" href="{href}">{label}</a>'

    def __init__(self, **kwargs):
        [setattr(self, k, kwargs.get('css_' + k, getattr(self, '_' + k)))
         for k in INIT_KEYS]

        self.size = self.adjust_size(self.size)
        self.align = self.adjust_align(self.align)
        self.extra = self.ajust_extra(self.extra)
        self.gap = self.gap.format(gap=self.gap_marker)
        self.head = self.head.format(size=self.size, align=self.align,
                                     extra=self.extra)

    def adjust_size(self, size=''):
        return self._size_prefix + size if size else ''

    def adjust_align(self, align=''):
        return self._align_prefix + align if align else ''

    def ajust_extra(self, extra=''):
        return self._extra_prefix + extra if extra else ''

    def get_normal(self, href='', label=''):
        return self.normal.format(href=href, label=label)

    def get_actived(self, href='', label=''):
        return self.actived.format(href=href, label=label)

    def get_side(self, href='#', disabled=False, side='prev'):
        if disabled:
            fmt = getattr(self, side + '_disabled')
        else:
            fmt = getattr(self, side + '_normal')

        return fmt.format(href=href, label=getattr(self, side + '_label'))

    def get_prev(self, href='', disabled=False):
        return self.get_side(href, disabled=disabled, side='prev')

    def get_next(self, href='', disabled=False):
        return self.get_side(href, disabled=disabled, side='next')
