# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-12 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors', '0002_auto_20170812_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default=1000),
            preserve_default=False,
        ),
    ]
