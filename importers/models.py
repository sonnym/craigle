from urllib.request import urlopen

from parsers.models import SiteParser
from cities.models import City

class SiteImporter():
    url = 'https://www.craigslist.org/about/sites'

    @classmethod
    def run(cls):
        response = urlopen(cls.url)
        html = response.read()

        cities = SiteParser().run(html)


        for city in cities:
            City.create_or_update(city)
