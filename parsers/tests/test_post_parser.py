from .base import ParserTestCase

from parsers.models import PostParser

class TestPostParser(ParserTestCase):
    def test_run(self):
        html = self.load_fixture('post')
        post = PostParser().run(html)

        self.assertEqual(post['title'], 'Ruby on Rails Software Developer')
        self.assertEqual(post['compensation'], 'Position pay range from $85 to $200 plus based on proven experience.')
