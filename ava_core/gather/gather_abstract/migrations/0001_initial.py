# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-06 02:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GatherHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('import_status', models.IntegerField(choices=[(0, 'Conpleted'), (1, 'Failed')], default=0)),
                ('message', models.CharField(max_length=500, null=True)),
                ('no_people', models.IntegerField(blank=True, null=True)),
                ('no_groups', models.IntegerField(blank=True, null=True)),
                ('no_identifiers', models.IntegerField(blank=True, null=True)),
                ('next_scheduled', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]