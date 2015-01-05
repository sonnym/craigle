from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class Post(models.Model):
    url = models.CharField(max_length=127, unique=True)
    title = models.CharField(max_length=255)
    compensation = models.CharField(max_length=255)

    @classmethod
    def create_or_update(cls, url):
        try:
            post = Post.objects.get(url=url)

        except ObjectDoesNotExist:
            post = Post(url=url)

        post.save()

        return post
