# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0002_auto_20170412_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='zip',
            name='cnt_workforce',
            field=models.IntegerField(null=True),
        ),
    ]
