# coding=utf-8

"""
Basic functional tests
"""

from selenium import webdriver
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class NewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    def test_home_title(self):
        self.browser.get(self.get_full_url('home'))
        self.assertIn('Unitech', self.browser.title)

    def test_css_works_ok(self):
        self.browser.get(self.get_full_url('home'))
        h1 = self.browser.find_element_by_tag_name('h1')
        self.assertEqual(h1.value_of_css_property('color'),
                         'rgba(51, 51, 51, 1)')
