# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-02 19:51
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merchant_dash', '0005_auto_20180402_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]