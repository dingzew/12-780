# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 06:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TaskID', models.CharField(max_length=8)),
                ('Description', models.CharField(max_length=30)),
                ('DueDate', models.CharField(max_length=8)),
                ('Status', models.CharField(max_length=5)),
            ],
        ),
    ]
