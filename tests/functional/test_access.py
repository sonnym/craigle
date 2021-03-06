from datetime import datetime

from django.test import TestCase, Client
from django.utils.timezone import utc

from posts.models import Post

class AccessTest(TestCase):
    def setup():
        self.client = Client()

    def test_access_root_path(self):
       response = self.client.get('/')

       self.assertEqual(200, response.status_code)

    def test_can_see_posts(self):
        Post(url='http://example.com/', title='Some Title', compensation='Some Compensation', posted_at=datetime.utcnow().replace(tzinfo=utc)).save()

        response = self.client.get('/')

        self.assertContains(response, 'Some Title', 1)
        self.assertContains(response, 'Some Compensation', 1)
