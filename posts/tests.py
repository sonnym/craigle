from datetime import datetime

from django.test import TestCase
from django.utils.timezone import utc

from posts.models import Post

class PostTest(TestCase):
    def test_create_or_update(self):
        url = 'foo'

        Post.create_or_update(url)
        self.assertEqual(1, Post.objects.count())

        Post.create_or_update(url)
        self.assertEqual(1, Post.objects.count())

    def test_posted_at_str(self):
        post = Post.create_or_update('foo')
        post.posted_at = datetime(2015, 1, 1, 0, 1).replace(tzinfo=utc)
        post.save()

        self.assertEqual('2015-01-01 00:01', post.posted_at_str)
