# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 21:15
from __future__ import unicode_literals
from django.db import migrations
from tcr_tools.geocode import get_city
from complaints.models import WageComplaint


class Migration(migrations.Migration):

    def add_city_to_complaint(apps,schema_editor):
        for wc in WageComplaint.objects.all():
            wc.claimaint_city = get_city(wc.claimant_zip_code)


    dependencies = [
        ('complaints', '0003_complaint_claimaint_city'),
    ]

    operations = [
            migrations.RunPyton(add_city_to_complaint)
    ]
