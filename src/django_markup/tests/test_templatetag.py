from __future__ import unicode_literals

import six
import os

from django.template.loader import render_to_string
from django.test import TestCase
from ..templatetags.markup_tags import apply_markup

from . import markup_strings as s


class PythonTemplateTagTestCase(TestCase):
    """
    Test the Templatetag conversion directly, without template rendering.

    No need to test all filters here, since their low level routines are
    covered in `test_filter`.
    """
    def test_none_filter(self):
        text, expected = s.NONE
        result = apply_markup(text, 'none')
        self.assertEqual(result, expected)

    def test_markdown_filter(self):
        text, expected = s.MARKDOWN
        result = apply_markup(text, 'markdown')
        self.assertEqual(result, expected)


class TemplateTagTestCase(TestCase):
    """
    Test the proper markup conversion using the template tag in a template itself.
    """

    def test_markdown_filter_with_templatetag(self):
        text, expected = s.MARKDOWN
        result = render_to_string('test_markdown.html', {
            'text': text, 'filter': 'markdown'})

        # Strip leading and trailing whitespace from the rendered HTL
        result = result.strip()

        self.assertEqual(result, expected)
