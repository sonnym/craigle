from django.test import TestCase, Client

class AccessTest(TestCase):
    def setup():
        self.client = Client()

    def test_access_root_path(self):
       response = self.client.get('/')

       self.assertEqual(200, response.status_code)
