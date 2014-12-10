from django.test import TestCase
from posts.models import Post

class PostTest(TestCase):
    def test_create_or_update(self):
        data = 'foo'

        Post.create_or_update(data)
        self.assertEqual(1, Post.objects.count())

        Post.create_or_update(data)
        self.assertEqual(1, Post.objects.count())
