# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-26 01:57
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('user_name', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True)),
                ('nick_name', models.CharField(default='New user', max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('email', models.EmailField(default='', max_length=254)),
                ('is_forbidden', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('problems_status', jsonfield.fields.JSONField(blank=True, default='{}', null=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
