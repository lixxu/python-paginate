#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals


class BaseCSS(object):
    def __init__(self, *args, **kwargs):
        self.size = kwargs.get('size') or ''
        self.align = kwargs.get('align') or ''
        if not self.align:
            self.align = kwargs.get('alignment') or ''

        self.prev_label = kwargs.get('prev_label') or '&laquo;'
        self.next_label = kwargs.get('next_label') or '&raquo;'
        self.gap_marker = kwargs.get('gap_marker') or '...'

    @property
    def css_head(self):
        return '<div>'

    @property
    def css_end(self):
        return '</div>'

    def get_normal(self, href='#', label=''):
        return '<a href="{0}">{1}</a>'.format(href, label)

    def get_disabled(self, label=''):
        return '<a class="disable">{0}</a>'.format(label)

    def get_actived(self, href='#', label=''):
        return '<a class="active" href="{0}">{1}</a>'.format(href, label)

    @property
    def gap(self):
        return self.gap_marker

    def get_side(self, href='#', label='', disabled=False):
        if disabled:
            return '<a class="disable">{0}</a>'.format(label)

        return '<a href="{0}">{1}</a>'.format(href, label)

    def get_prev(self, href='#', disabled=False):
        return self.get_side(href, label=self.prev_label, disabled=disabled)

    def get_next(self, href='#', disabled=False):
        return self.get_side(href, label=self.next_label, disabled=disabled)
