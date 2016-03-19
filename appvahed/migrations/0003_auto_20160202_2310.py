# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-02 19:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appvahed', '0002_mdl_vahed_lname'),
    ]

    operations = [
        migrations.CreateModel(
            name='mdl_sakhtemoun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='mdl_vahed',
            name='sakhtemoun',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='appvahed.mdl_sakhtemoun'),
            preserve_default=False,
        ),
    ]
