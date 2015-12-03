# coding=utf-8

"""
Unittests
"""

from django.core.urlresolvers import reverse
from django.test import TestCase


class HomePageTest(TestCase):

    def test_uses_index_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'unitech/index.html')

    def test_uses_base_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'base.html')
