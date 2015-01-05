from unittest.mock import Mock, patch
from django.test import TestCase

import django_rq

from importers.models import SiteImporter, CityImporter, PostImporter
from parsers.models import SiteParser, CityParser, PostParser

from cities.models import City
from posts.models import Post

class SiteImporterTest(TestCase):
    def test_run(self):
        cities = [{ 'name': 'foo', 'url': 'bar' }]

        with patch.object(SiteParser, 'run', return_value=cities):
            with patch.object(City, 'create_or_update') as mock_city_create_or_update:
                with patch.object(django_rq, 'enqueue') as mock_django_rq_enqueue:
                    SiteImporter.run()

                    mock_city_create_or_update.assert_called_once_with(cities[0])

                    mock_django_rq_enqueue.assert_called

class CityImporterTest(TestCase):
    def test_run(self):
        city = Mock(url='http://nyc.craigslist.org/')
        posts = ['/foo/bar']

        with patch.object(CityParser, 'run', return_value=posts):
            with patch.object(Post, 'create_or_update') as mock_post_create_or_update:
                with patch.object(django_rq, 'enqueue') as mock_django_rq_enqueue:
                    CityImporter.run(city)

                    mock_post_create_or_update.assert_called_once_with('http://nyc.craigslist.org/foo/bar')

                    mock_django_rq_enqueue.assert_called

class PostImporterTest(TestCase):
    def test_run(self):
        post_data = { 'title': 'Some Title', 'compensation': 'Some Compensation' }

        with patch.object(PostParser, 'run', return_value=post_data):
            post = Mock(url='http://example.com/')

            PostImporter.run(post)

            post.save.assert_called_once_with()
