from .base import ParserTestCase

from parsers.models import CityParser

class TestCityParser(ParserTestCase):
    def test_run(self):
        html = self.load_fixture('jjj_start')
        posts = CityParser().run(html)

        self.assertEqual(len(posts), 100)
        all(map(lambda post: self.assertIsInstance(post, str), posts))
