# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0002_auto_20170411_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='claimaint_city',
            field=models.TextField(null=True),
        ),
    ]
