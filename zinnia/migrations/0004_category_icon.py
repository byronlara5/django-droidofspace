# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-10 15:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('zinnia', '0003_publication_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.CharField(default=datetime.datetime(2016, 3, 10, 15, 4, 1, 403000, tzinfo=utc), max_length=255, verbose_name='icon'),
            preserve_default=False,
        ),
    ]
