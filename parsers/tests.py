import os.path

from django.test import TestCase
from django.core.validators import URLValidator

from cities.models import City
from parsers.models import SiteParser, CityParser, PostParser

class ParserTestCase(TestCase):
    def load_fixture(self, name):
        fixture = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_fixtures', name)

        with open(fixture, 'r') as f:
            value = f.read()

        return value

class TestSiteParser(ParserTestCase):
    def test_run(self):
        html = self.load_fixture('sites')
        cities = SiteParser().run(html)

        self.assertEqual(len(cities), 714)
        all(map(lambda city: self.assertIsInstance(city, dict), cities))

        all(map(lambda city, v=URLValidator(schemes=['https']): v(city['url']), cities))

class TestCityParser(ParserTestCase):
    def test_run(self):
        city = City(url='https://foo.bar/')

        html = self.load_fixture('jjj_start')
        posts = CityParser().run(city, html)

        self.assertEqual(len(posts), 100)
        all(map(lambda post: self.assertIsInstance(post, str), posts))

        all(map(lambda post, v=URLValidator(schemes=['https']): v(post), posts))

class TestPostParser(ParserTestCase):
    def test_run(self):
        html = self.load_fixture('post')
        post = PostParser().run(html)

        self.assertEqual(post['title'], 'PT Community Support Professional (After School) (Newfield)')
        self.assertEqual(post['compensation'], 'Starting pay is $11.00 to $11.50 per hour')
