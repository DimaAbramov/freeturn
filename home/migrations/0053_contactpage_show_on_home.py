# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-25 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0052_auto_20190115_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='show_on_home',
            field=models.BooleanField(default=False, help_text='Show link to this form on home page?'),
        ),
    ]