from datetime import date
from functools import total_ordering

from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import URLValidator

class Post(models.Model):
    url = models.CharField(max_length=127, unique=True, validators=[URLValidator(schemes=['http'])])
    title = models.CharField(max_length=255)
    compensation = models.CharField(max_length=255)

    posted_at = models.DateTimeField(null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    @classmethod
    def create_or_update(cls, url):
        try:
            post = Post.objects.get(url=url)

        except ObjectDoesNotExist:
            post = Post(url=url)

        post.save()

        return post

    @property
    def posted_at_str(self):
        if self.posted_at:
            return self.posted_at.strftime('%Y-%m-%d %H:%M')
        else:
            return 'N/A'

    @property
    def posted_at_date(self):
        if self.posted_at:
            return date(self.posted_at.year, self.posted_at.month, self.posted_at.day)
        else:
            return None

@total_ordering
class DatedPosts():
    def __init__(self, date, posts):
        self.date = date
        self.posts = posts

    def __eq__(self, other):
        return self.date == other.date

    def __lt__(self, other):
        return self.date > other.date

    @property
    def date_str(self):
        return self.date.strftime("%Y-%m-%d")
