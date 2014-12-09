from lxml import html

class SiteParser():
    def run(self, contents):
        tree = html.document_fromstring(contents)
        cities = tree.cssselect('section.body ul li a')

        return [{ 'name': city.text_content(), 'url': city.get('href') } for city in cities]

class CityParser():
    def run(self, contents):
        tree = html.document_fromstring(contents)
        posts = tree.cssselect('div.rightpane p.row > a')

        return [post.get('href') for post in posts]
