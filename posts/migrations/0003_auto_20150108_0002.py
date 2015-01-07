# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20150105_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 8, 0, 2, 57, 962259, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 1, 8, 0, 2, 57, 962311, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
