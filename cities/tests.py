from django.test import TestCase
from cities.models import City

class CityTest(TestCase):
    def test_create_or_update(self):
        data = { 'name': 'foo', 'url': 'bar' }

        City.create_or_update(data)
        self.assertEqual(1, City.objects.count())

        City.create_or_update(data)
        self.assertEqual(1, City.objects.count())
