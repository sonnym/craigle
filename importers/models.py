from urllib.parse import urljoin
from urllib.request import urlopen

from parsers.models import SiteParser, CityParser
from cities.models import City
from posts.models import Post

class SiteImporter():
    url = 'https://www.craigslist.org/about/sites'

    @classmethod
    def run(cls):
        response = urlopen(cls.url)
        html = response.read()

        cities = SiteParser().run(html)


        for city in cities:
            City.create_or_update(city)

class CityImporter():
    path = 'search/jjj/?cat_id=14&cat_id=21&cat_id=11&is_telecommuting=1&is_contract=1'

    @classmethod
    def run(cls, City):
        # import pdb; pdb.set_trace()

        response = urlopen(urljoin(City.url, cls.path, allow_fragments=True))
        html = response.read()

        posts = CityParser().run(html)

        for post in posts:
            Post.create_or_update(urljoin(City.url, post))
