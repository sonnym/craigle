from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class City(models.Model):
    name = models.CharField(max_length=127)
    url = models.CharField(max_length=127)

    @classmethod
    def create_or_update(cls, city_data):
        try:
            city = City.objects.get(name=city_data['name'])
            city.url = city_data['url']

        except ObjectDoesNotExist:
            city = City(**city_data)

        city.save()

        return city
