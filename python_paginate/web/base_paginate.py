#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys

_basestring = str if (sys.version_info[0] == 3) else basestring


class BasePagination(object):
    """A simple pagination for web frameworks."""
    _css_framework = 'bootstrap'
    _css = None  # css framework instance
    _page_name = 'page'
    _per_page_name = 'per_page'
    _max_per_page = 100  # prevent malicious user to load too many records
    _hide_page_one = True
    _inner_window = 2
    _outer_window = 1
    _format_total = False
    _format_number = False
    _show_prev = True
    _show_next = True
    _record_name = 'records'
    _href = None
    _search = False
    _show_single_page = False
    _display_msg = 'displaying <b>{start} - {end}</b> {record_name} in \
    total <b>{total}</b>'
    _search_msg = 'found <b>{total}</b> {record_name} \
    displaying <b>{start} - {end}</b>'
    _info_head = '<div class="pagination-page-info">'
    _info_end = '</div>'

    def __init__(self, *args, **kwargs):
        """Detail parameters remark.

        **url**: current request url

        **page_name**: arg name for page, default is `page`

        **page**: current page

        **per_page_name**: arg name for per_page, default is `per_page`

        **per_page**: how many records displayed on one page

        **hide_page_one**: hide page=1 or /page/1 in url

        **search**: search or not?

        **total**: total records for pagination

        **display_msg**: text for pagation information

        **search_msg**: text for search information

        **info_head**: CSS for pagination info head

        **info_end**: CSS for pagination info end

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

        **show_prev**: show previous page or not

        **show_next**: show next page or not

        **others**: other parameters startswith css_ will be accepted by \
        css_framework
        """
        self.page_name = kwargs.get('page_name', self._page_name)
        self.per_page_name = kwargs.get('per_page_name', self._per_page_name)
        self.page = kwargs.get(self.page_name, 1)
        self.per_page = kwargs.get(self.per_page_name, 10)
        self.max_per_page = kwargs.get('max_per_page', self._max_per_page)
        if self.per_page > self.max_per_page:
            self.per_page = self.max_per_page

        self.total = kwargs.get('total', 0)

        self.hide_page_one = kwargs.get('hide_page_one', self._hide_page_one)
        self.inner_window = kwargs.get('inner_window', self._inner_window)
        self.outer_window = kwargs.get('outer_window', self._outer_window)

        self.search = kwargs.get('search', self._search)
        self.format_total = kwargs.get('format_total', self._format_total)
        self.format_number = kwargs.get('format_number', self._format_number)
        self.display_msg = kwargs.get('display_msg', self._display_msg)
        self.search_msg = kwargs.get('search_msg', self._search_msg)
        self.info_head = kwargs.get('info_head', self._info_head)
        self.info_end = kwargs.get('info_end', self._info_end)

        self.show_prev = kwargs.get('show_prev', self._show_prev)
        self.show_next = kwargs.get('show_next', self._show_next)
        self.record_name = kwargs.get('record_name', self._record_name)
        self.href = kwargs.get('href', self._href)
        self.show_single_page = kwargs.get('show_single_page',
                                           self._show_single_page)
        self.css = self.get_css(kwargs.pop('css_framework', None), **kwargs)
        self.url = kwargs.get('url') or self.get_url()
        self.init_values()

    def init_values(self):
        self._cached = {}
        self.skip = (self.page - 1) * self.per_page
        pages = divmod(self.total, self.per_page)
        self.total_pages = pages[0] + 1 if pages[1] else pages[0]

        self.has_prev = self.page > 1
        self.has_next = self.page < self.total_pages

    def get_css(self, css_framework=None, **kwargs):
        if self._css:
            return self._css

        if not css_framework:
            css_framework = self._css_framework

        if isinstance(css_framework, _basestring):
            if 'semantic' in css_framework:
                import python_paginate.css.semantic as semantic
                css_class = semantic.Semantic
            elif 'foundation' in css_framework:
                import python_paginate.css.foundation as foundation
                css_class = foundation.Foundation
            elif css_framework == 'ink':
                import python_paginate.css.ink as ink
                css_class = ink.Ink
            elif css_framework == 'uikit':
                import python_paginate.css.uikit as uikit
                css_class = uikit.UIKit
            elif 'bootstrap' in css_framework:
                import python_paginate.css.bootstrap as bootstrap
                if '2' in css_framework:
                    css_class = bootstrap.Bootstrap2
                elif '3' in css_framework:
                    css_class = bootstrap.Bootstrap3
                elif '4' in css_framework:
                    css_class = bootstrap.Bootstrap4
                else:
                    css_class = bootstrap.Bootstrap3
            else:
                import python_paginate.css.bootstrap as bootstrap
                css_class = bootstrap.Bootstrap3
        else:
            css_class = css_framework

        self.__class__._css = css_class(**kwargs)
        return self._css

    def get_url(self):
        """Flask can get from request."""
        return ''

    def get_href(self, page=1):
        if self.href:
            return self.href.format(page or 1)

        text = '/{}/'.format(self.page_name)
        if text in self.url:
            current_page = '{}{}'.format(text, self.page)
            new_page = '{}{}'.format(text, page)
            if self.hide_page_one and page == 1:
                new_page = ''

            return self.url.replace(current_page, new_page)

        new_page = '{}={}'.format(self.page_name, page)
        if self.hide_page_one and page == 1:
            new_page = ''

        text = '{}='.format(self.page_name)
        if '?' in self.url:
            base_url, querys = self.url.split('?', 1)
            qs = [q for q in querys.split('&') if not q.startswith(text)]
            if new_page:
                qs.append(new_page)

            return '{}?{}'.format(base_url, '&'.join(qs))

        if new_page:
            return '{}?{}'.format(self.url, new_page)

        return self.url

    @property
    def raw_single_link(self):
        if 'single' not in self._cached:
            links = [self.css.head]
            if self.show_prev:
                links.append(self.css.get_prev(disabled=True))

            links.append(self.css.get_actived(label=1))
            if self.show_next:
                links.append(self.css.get_next(disabled=True))

            links.append(self.css.end)
            self._cached['single'] = ''.join(links)

        return self._cached['single']

    @property
    def single_link(self):
        """You can do markup here, such as flask has Markup(links_text)."""
        return self.raw_single_link

    @property
    def raw_links(self):
        if 'links' in self._cached:
            return self._cached['links']

        if self.total_pages <= 1:
            if self.show_single_page:
                self._cached['links'] = self.raw_single_link
            else:
                self._cached['links'] = ''

            return self._cached['links']

        links = [self.css.head]
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

        links.append(self.css.end)
        self._cached['links'] = ''.join(links)
        return self._cached['links']

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
        if 'info' in self._cached:
            return self._cached['info']

        start = 1 + (self.page - 1) * self.per_page
        end = start + self.per_page - 1
        if end > self.total:
            end = self.total

        if start > self.total:
            start = self.total

        links = [self.info_head]
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
        links.append(self.info_end)
        self._cached['info'] = ''.join(links)
        return self._cached['info']

    @property
    def info(self):
        """You can do markup here, such as flask Markup(links_text)."""
        return self.raw_info
