from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import URLValidator

class City(models.Model):
    name = models.CharField(max_length=127, unique=True)
    url = models.CharField(max_length=127, validators=[URLValidator(schemes=['http'])])

    @classmethod
    def create_or_update(cls, city_data):
        try:
            city = City.objects.get(name=city_data['name'])
            city.url = city_data['url']

        except ObjectDoesNotExist:
            city = City(**city_data)

        city.save()

        return city
