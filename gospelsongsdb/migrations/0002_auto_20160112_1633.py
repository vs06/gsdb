# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gospelsongsdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Culto',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('date', models.DateField(null=True, blank=True, verbose_name='data')),
            ],
        ),
        migrations.CreateModel(
            name='Musica',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('tune', models.CharField(max_length=10, verbose_name='tom')),
                ('band', models.CharField(max_length=100, verbose_name='artista')),
                ('lyrics', models.CharField(max_length=255, verbose_name='letra')),
                ('link', models.URLField(max_length=255, verbose_name='link')),
                ('obs', models.TextField(verbose_name='obs')),
                ('datashow', models.CharField(max_length=1, verbose_name='datashow')),
            ],
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='campi',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='songs',
        ),
        migrations.AlterField(
            model_name='campi',
            name='address',
            field=models.CharField(max_length=200, verbose_name='endereco'),
        ),
        migrations.AlterField(
            model_name='campi',
            name='capacity',
            field=models.IntegerField(verbose_name='capacidade'),
        ),
        migrations.AlterField(
            model_name='campi',
            name='name',
            field=models.CharField(max_length=100, verbose_name='nome'),
        ),
        migrations.DeleteModel(
            name='Meeting',
        ),
        migrations.DeleteModel(
            name='Song',
        ),
        migrations.AddField(
            model_name='culto',
            name='campi',
            field=models.ForeignKey(verbose_name='local', db_column='campi', null=True, blank=True, to='gospelsongsdb.Campi'),
        ),
        migrations.AddField(
            model_name='culto',
            name='songs',
            field=models.ForeignKey(verbose_name='musicas', db_column='songs', null=True, blank=True, to='gospelsongsdb.Musica'),
        ),
    ]
