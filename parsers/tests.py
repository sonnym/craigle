import os.path

from django.test import TestCase

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

        self.assertEqual(len(cities), 712)
        all(map(lambda city: self.assertIsInstance(city, dict), cities))

class TestCityParser(ParserTestCase):
    def test_run(self):
        html = self.load_fixture('jjj_start')
        posts = CityParser().run(html)

        self.assertEqual(len(posts), 100)
        all(map(lambda post: self.assertIsInstance(post, str), posts))

class TestPostParser(ParserTestCase):
    def test_run(self):
        html = self.load_fixture('post')
        post = PostParser().run(html)

        self.assertEqual(post['title'], 'Ruby on Rails Software Developer')
        self.assertEqual(post['compensation'], 'Position pay range from $85 to $200 plus based on proven experience.')
