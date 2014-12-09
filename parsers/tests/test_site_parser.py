from .base import ParserTestCase

from parsers.models import SiteParser

class TestSiteParser(ParserTestCase):
    def test_run(self):
        html = self.load_fixture('sites')
        cities = SiteParser().run(html)

        self.assertEqual(len(cities), 712)
        all(map(lambda city: self.assertIsInstance(city, dict), cities))
