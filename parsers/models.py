from urllib.parse import urlparse, urljoin

from datetime import datetime
from lxml import html

class SiteParser():
    def run(self, contents):
        tree = html.document_fromstring(contents)
        cities = tree.cssselect('section.body ul li a')

        return [{ 'name': city.text_content(), 'url': URLParser.ensure_url_scheme(city.get('href')) } for city in cities]

class CityParser():
    def run(self, city, contents):
        tree = html.document_fromstring(contents)
        posts = tree.cssselect('div#sortable-results p.row > a')

        city_parsed_url = urlparse(city.url)
        city_base_url = city_parsed_url.scheme + '://' + city_parsed_url.netloc

        return [URLParser.ensure_url_scheme(urljoin(city_base_url, post.get('href'))) for post in posts]

class PostParser():
    def run(self, contents):
        tree = html.document_fromstring(contents)

        title = str(tree.cssselect('span#titletextonly')[0].text_content()).strip()
        compensation = tree.cssselect('div.mapAndAttrs p.attrgroup b')[0].text

        posted_at = tree.cssselect('p#display-date time')[0].get('datetime')
        parsed_posted_at = datetime.strptime(posted_at, '%Y-%m-%dT%H:%M:%S%z')

        return { 'title': title, 'compensation': compensation, 'posted_at': parsed_posted_at }

class URLParser():
    @staticmethod
    def ensure_url_scheme(urlish):
        parsed_url = urlparse(urlish)

        if parsed_url.scheme == '':
            return urljoin('https://' + parsed_url.netloc, parsed_url.path)
        else:
            return urlish
