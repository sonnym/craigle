# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20150108_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 8, 1, 20, 57, 207650, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 1, 8, 1, 20, 57, 207672, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
