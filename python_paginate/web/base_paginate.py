#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

RECORD_NAME = 'records'
DISPLAY_MSG = 'displaying <b>{start} - {end}</b> {record_name} in \
total <b>{total}</b>'
SEARCH_MSG = 'found <b>{total}</b> {record_name} \
displaying <b>{start} - {end}</b>'
PAGE_INFO_HEAD = '<div class="pagination-page-info">'
PAGE_INFO_END = '</div>'


class BasePagination(object):
    """A simple pagination for tornado."""

    def __init__(self, *args, **kwargs):
        """Detail parameters remark.

        **url**: current request url

        **page**: current page

        **per_page**: how many records displayed on one page

        **hide_page_one**: hide page=1 or /page/1 in url

        **search**: search or not?

        **total**: total records for pagination

        **display_msg**: text for pagation information

        **search_msg**: text for search information

        **page_info_head**: CSS for pagination info head

        **page_info_end**: cSS for pagination info end

        **record_name**: record name showed in pagination information

        **href**: Add custom href for links - this supports forms \
        with post method

        **show_single_page**: decide whether or not a single page \
        returns pagination

        **href**: <a> href parameter, MUST contain {0} to format \
        page number

        **format_total**: number format total, like **1,234**, \
        default is False

        **format_number**: number format start and end, like **1,234**, \
        default is False

        **inner_window**: how many links arround current page

        **outer_window**: how many links near first/last link

        **css_framework**: the css framework, default is **bootstrap**

        **size**: font size of page links

        **align**: the alignment of pagination links

        **prev_label**: text for previous page, default is **&laquo;**

        **next_label**: text for next page, default is **&raquo;**

        **show_prev**: show previous page or not

        **show_next**: show next page or not
        """
        self.url = kwargs.get('url') or self.get_url()
        self.page = kwargs.get('page', 1)
        self.per_page = kwargs.get('per_page', 10)
        self.hide_page_one = kwargs.get('hide_page_one', True)
        self.inner_window = kwargs.get('inner_window', 2)
        self.outer_window = kwargs.get('outer_window', 1)

        self.search = kwargs.get('search', False)
        self.total = kwargs.get('total', 0)
        self.format_total = kwargs.get('format_total', False)
        self.format_number = kwargs.get('format_number', False)
        self.display_msg = kwargs.get('display_msg') or DISPLAY_MSG
        self.search_msg = kwargs.get('search_msg') or SEARCH_MSG
        self.page_info_head = kwargs.get('page_info_head') or PAGE_INFO_HEAD
        self.page_info_end = kwargs.get('page_info_end') or PAGE_INFO_END

        self.show_prev = kwargs.get('show_prev', True)
        self.show_next = kwargs.get('show_next', True)
        self.record_name = kwargs.get('record_name') or RECORD_NAME
        self.href = kwargs.get('href', None)
        self.show_single_page = kwargs.get('show_single_page', False)

        css_framework = kwargs.get('css_framework', 'semantic').lower()
        self.css = self.get_css_class(css_framework)(**kwargs)
        self.init_values()

    def init_values(self):
        self.skip = (self.page - 1) * self.per_page
        pages = divmod(self.total, self.per_page)
        self.total_pages = pages[0] + 1 if pages[1] else pages[0]

        self.has_prev = self.page > 1
        self.has_next = self.page < self.total_pages

    def get_css_class(self, css_framework):
        if 'semantic' in css_framework:
            from python_paginate.css.semanticui import SemanticUI
            return SemanticUI
        elif 'foundation' in css_framework:
            from python_paginate.css.foundation import Foundation
            return Foundation
        elif 'bootstrap' in css_framework:
            import python_paginate.css.bootstrap as bootstrap
            if '2' in css_framework:
                return bootstrap.Bootstrap2
            elif '3' in css_framework:
                return bootstrap.Bootstrap3
            elif '4' in css_framework:
                return bootstrap.Bootstrap4
            else:
                return bootstrap.Bootstrap3
        else:
            from python_paginate.css.semanticui import SemanticUI
            return SemanticUI

    def get_url(self):
        """Flask can get from request."""
        return ''

    def get_href(self, page=1):
        if self.href:
            return self.href.format(page or 1)

        if '/page/' in self.url:
            current_page = '/page/{}'.format(self.page)
            new_page = '/page/{}'.format(page)
            if self.hide_page_one and page == 1:
                new_page = ''

            return self.url.replace(current_page, new_page)

        new_page = 'page={}'.format(page)
        if self.hide_page_one and page == 1:
            new_page = ''

        if '?' in self.url:
            base_url, querys = self.url.split('?', 1)
            qs = [q for q in querys.split('&') if not q.startswith('page=')]
            if new_page:
                qs.append(new_page)

            return '{}?{}'.format(base_url, '&'.join(qs))

        if new_page:
            return '{}?{}'.format(self.url, new_page)

        return self.url

    @property
    def raw_single_link(self):
        links = [self.css.css_head]
        if self.show_prev:
            links.append(self.css.get_prev(disabled=True))

        links.append(self.css.get_actived(label=1))
        if self.show_next:
            links.append(self.css.get_next(disabled=True))

        links.append(self.css.css_end)
        return ''.join(links)

    @property
    def single_link(self):
        """You can do markup here, such as flask has Markup(links_text)."""
        return self.raw_single_link

    @property
    def raw_links(self):
        if self.total_pages <= 1:
            if self.show_single_page:
                return self.raw_single_link

            return ''

        links = [self.css.css_head]
        if self.show_prev:
            # previous page link
            href = self.get_href(self.page - 1)
            disabled = not self.has_prev
            links.append(self.css.get_prev(href=href, disabled=disabled))

        # page links
        for page in self.pages:
            if page is None:
                links.append(self.css.gap)
                continue

            href = self.get_href(page)
            if page == self.page:  # active page
                links.append(self.css.get_actived(href=href, label=page))
            else:
                links.append(self.css.get_normal(href=href, label=page))

        if self.show_next:
            # next page link
            href = self.get_href(self.page + 1)
            disabled = not self.has_next
            links.append(self.css.get_next(href=href, disabled=disabled))

        links.append(self.css.css_end)

        return ''.join(links)

    @property
    def links(self):
        """You can do markup here, such as flask has Markup(links_text)."""
        return self.raw_links

    @property
    def pages(self):
        if self.total_pages < self.inner_window * 2 - 1:
            return range(1, self.total_pages + 1)

        pages = []
        win_from = self.page - self.inner_window
        win_to = self.page + self.inner_window
        if win_to > self.total_pages:
            win_from -= win_to - self.total_pages
            win_to = self.total_pages

        if win_from < 1:
            win_to = win_to + 1 - win_from
            win_from = 1
            if win_to > self.total_pages:
                win_to = self.total_pages

        if win_from > self.inner_window:
            pages.extend(range(1, self.outer_window + 1 + 1))
            pages.append(None)
        else:
            pages.extend(range(1, win_to + 1))

        if win_to < self.total_pages - self.inner_window + 1:
            if win_from > self.inner_window:
                pages.extend(range(win_from, win_to + 1))

            pages.append(None)
            pages.extend(range(self.total_pages - 1, self.total_pages + 1))
        elif win_from > self.inner_window:
            pages.extend(range(win_from, self.total_pages + 1))
        else:
            pages.extend(range(win_to + 1, self.total_pages + 1))

        return pages

    @property
    def raw_info(self):
        """Get the pagination information."""
        start = 1 + (self.page - 1) * self.per_page
        end = start + self.per_page - 1
        if end > self.total:
            end = self.total

        if start > self.total:
            start = self.total

        links = [self.page_info_head]
        page_msg = self.search_msg if self.search else self.display_msg
        if self.format_total:
            total_text = '{0:,}'.format(self.total)
        else:
            total_text = '{0}'.format(self.total)

        if self.format_number:
            start_text = '{0:,}'.format(start)
            end_text = '{0:,}'.format(end)
        else:
            start_text = start
            end_text = end

        links.append(page_msg.format(total=total_text,
                                     start=start_text,
                                     end=end_text,
                                     record_name=self.record_name,
                                     )
                     )
        links.append(self.page_info_end)
        return ''.join(links)

    @property
    def info(self):
        """You can do markup here, such as flask Markup(links_text)."""
        return self.raw_info
