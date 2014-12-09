from unittest.mock import Mock, patch
from django.test import TestCase

from importers.models import SiteImporter
from parsers.models import SiteParser
from cities.models import City

class SiteImporterTest(TestCase):
    def test_run(self):
        cities = [{ 'name': 'foo', 'url': 'bar' }]

        mock = Mock(City.create_or_update)
        City.create_or_update = mock

        with patch.object(SiteParser, 'run', return_value=cities) as mock_method:
            SiteImporter.run()

            mock.assert_called_once_with(cities[0])
