import os.path

from django.test import TestCase

class ParserTestCase(TestCase):
    def load_fixture(self, name):
        fixture = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fixtures', name)

        with open(fixture, 'r') as f:
            value = f.read()

        return value
