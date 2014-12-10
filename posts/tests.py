from django.test import TestCase
from posts.models import Post

class PostTest(TestCase):
    def test_create_or_update(self):
        url = 'foo'

        Post.create_or_update(url)
        self.assertEqual(1, Post.objects.count())

        Post.create_or_update(url)
        self.assertEqual(1, Post.objects.count())
