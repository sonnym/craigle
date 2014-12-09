from unittest.mock import Mock, patch
from django.test import TestCase

from importers.models import CityImporter
from parsers.models import CityParser
from cities.models import City

class CityImporterTest(TestCase):
    def test_run(self):
        cities = [{ 'name': 'foo', 'url': 'bar' }]

        mock = Mock(City.create_or_update)
        City.create_or_update = mock

        with patch.object(CityParser, 'run', return_value=cities) as mock_method:
            CityImporter.run()

            mock.assert_called_once_with(cities[0])
