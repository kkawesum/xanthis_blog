# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-04 16:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170904_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 4, 16, 12, 54, 612820, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 4, 16, 12, 54, 612820, tzinfo=utc)),
        ),
    ]
