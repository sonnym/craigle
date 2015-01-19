from datetime import datetime, timedelta

from urllib.parse import urljoin
from urllib.request import urlopen

import django_rq

from parsers.models import SiteParser, CityParser, PostParser

from cities.models import City
from posts.models import Post

class SiteImporter():
    url = 'https://www.craigslist.org/about/sites'

    @classmethod
    def run(cls):
        response = urlopen(cls.url)
        html = response.read()

        cities = SiteParser().run(html)

        for city_data in cities:
            city = City.create_or_update(city_data)
            django_rq.enqueue(CityImporter.run, city)

        nextrun = datetime.now() + timedelta(hours=6)
        django_rq.get_scheduler('default').enqueue_at(nextrun, SiteImporter.run)

class CityImporter():
    path = 'search/jjj/?cat_id=14&cat_id=21&cat_id=11&is_telecommuting=1&is_contract=1'

    @classmethod
    def run(cls, city):
        response = urlopen(urljoin(city.url, cls.path, allow_fragments=True))
        html = response.read()

        posts = CityParser().run(html)

        for post_data in posts:
            post = Post.create_or_update(urljoin(city.url, post_data))
            django_rq.enqueue(PostImporter.run, post)

class PostImporter():
    @classmethod
    def run(cls, post):
        if post.title:
            return

        response = urlopen(post.url)
        html = response.read()

        post_data = PostParser().run(html)

        post.title = post_data['title']
        post.compensation = post_data['compensation']

        post.posted_at = post_data['posted_at']

        post.save()
