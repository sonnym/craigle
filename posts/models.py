from datetime import datetime

from django.db import models
from django.core.exceptions import ObjectDoesNotExist

from django.utils.timezone import utc

class Post(models.Model):
    url = models.CharField(max_length=127, unique=True)
    title = models.CharField(max_length=255)
    compensation = models.CharField(max_length=255)

    posted_at = models.DateTimeField(null=True)

    created_at = models.DateTimeField(auto_now_add=True, default=datetime.utcnow().replace(tzinfo=utc), null=False)
    updated_at = models.DateTimeField(auto_now=True, default=datetime.utcnow().replace(tzinfo=utc), null=False)

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
