# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0002_auto_20150105_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='url',
            field=models.CharField(validators=[django.core.validators.URLValidator(schemes=['http'])], max_length=127),
        ),
    ]
