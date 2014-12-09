import os.path

from django.test import TestCase
from parsers.models import SiteParser

class TestSiteParser(TestCase):
    def test_run(self):
        fixture = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fixtures', 'sites')
        with open(fixture, 'r') as f:
            html = f.read()

        cities = SiteParser().run(html)

        self.assertEqual(len(cities), 712)
        all(map(lambda city: self.assertIsInstance(city, dict), cities))
