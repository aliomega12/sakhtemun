# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-19 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appvahed', '0009_auto_20160319_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mdl_vahed',
            name='metraj',
            field=models.CharField(max_length=128, verbose_name='\u0645\u062a\u0631\u0627\u0698'),
        ),
    ]
