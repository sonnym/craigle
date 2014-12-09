import os.path

from django.test import TestCase
from parsers.models import CityParser

class TestCityParser(TestCase):
    def test_run(self):
        fixture = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fixtures', 'sites')
        with open(fixture, 'r') as f:
            html = f.read()

        cities = CityParser().run(html)

        self.assertEqual(len(cities), 712)
        all(map(lambda city: self.assertIsInstance(city, dict), cities))
