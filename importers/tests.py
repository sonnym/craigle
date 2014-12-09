from unittest.mock import Mock, patch
from django.test import TestCase

from importers.models import SiteImporter, CityImporter
from parsers.models import SiteParser, CityParser

from cities.models import City
from posts.models import Post

class SiteImporterTest(TestCase):
    def test_run(self):
        cities = [{ 'name': 'foo', 'url': 'bar' }]

        mock = Mock(City.create_or_update)
        City.create_or_update = mock

        with patch.object(SiteParser, 'run', return_value=cities) as mock_method:
            SiteImporter.run()

            mock.assert_called_once_with(cities[0])

class CityImporterTest(TestCase):
    def test_run(self):
        city = Mock(url='http://nyc.craigslist.org/')
        posts = ['/foo/bar']

        mock = Mock(Post.create_or_update)
        Post.create_or_update = mock

        with patch.object(CityParser, 'run', return_value=posts) as mock_method:
            CityImporter.run(city)

            mock.assert_called_once_with('http://nyc.craigslist.org/foo/bar')
