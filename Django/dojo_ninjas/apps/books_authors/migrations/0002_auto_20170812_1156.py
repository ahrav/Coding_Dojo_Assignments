# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-12 11:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='authors',
            new_name='Author',
        ),
    ]