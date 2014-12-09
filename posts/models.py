from django.db import models

class Post(models.Model):
    @classmethod
    def create_or_update(cls, url):
        pass
