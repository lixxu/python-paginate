#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import basecss


class SemanticUICSS(basecss.BaseCSS):
    normal_fmt = '<a class="item" href="{href}">{label}</a>'
    actived_fmt = '<a class="active item">{label}</a>'
    disabled_fmt = '<div class="disabled item">{label}</div>'
    prev_label = '<i class="left arrow icon"></i>'
    next_label = '<i class="right arrow icon"></i>'
    prev_next_disabled_fmt = '<div class="disabled icon item">{label}</div>'
    prev_next_normal_fmt = '<a class="icon item" href="{href}">{label}</a>'
    css_head_fmt = '<div class="ui pagination {size}{align}menu">'

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('prev_label', self.prev_label)
        kwargs.setdefault('next_label', self.next_label)
        super(SemanticUICSS, self).__init__(*args, **kwargs)

    @property
    def css_head(self):
        if self.size:
            self.size = self.size + ' '

        if self.align:
            self.align = self.align + ' '

        return self.css_head_fmt.format(size=self.size, align=self.align)

    def get_normal(self, href='#', label=''):
        return self.normal_fmt.format(href=href, label=label)

    def get_disabled(self, label=''):
        return self.disabled_fmt.format(label=label)

    def get_actived(self, href='#', label=''):
        return self.actived_fmt.format(href=href, label=label)

    @property
    def gap(self):
        return self.get_disabled(self.gap_marker)

    def get_side(self, href='#', label='', disabled=False):
        if disabled:
            fmt = self.prev_next_disabled_fmt
        else:
            fmt = self.prev_next_normal_fmt

        return fmt.format(href=href, label=label)

    def get_prev(self, href='#', disabled=False):
        return self.get_side(href, label=self.prev_label, disabled=disabled)

    def get_next(self, href='#', disabled=False):
        return self.get_side(href, label=self.next_label, disabled=disabled)
