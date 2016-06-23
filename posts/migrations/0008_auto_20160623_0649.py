# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20150108_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.CharField(validators=[django.core.validators.URLValidator(schemes=['http'])], max_length=127, unique=True),
        ),
    ]
