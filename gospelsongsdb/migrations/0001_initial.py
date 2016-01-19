# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campi',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('date', models.DateField(null=True, blank=True)),
                ('campi', models.ForeignKey(to='gospelsongsdb.Campi', null=True, db_column='campi', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('tune', models.CharField(max_length=10)),
                ('band', models.CharField(max_length=100)),
                ('lyrics', models.CharField(max_length=255)),
                ('link', models.URLField(max_length=255)),
                ('obs', models.TextField()),
                ('datashow', models.CharField(max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='meeting',
            name='songs',
            field=models.ForeignKey(to='gospelsongsdb.Song', null=True, db_column='songs', blank=True),
        ),
    ]
