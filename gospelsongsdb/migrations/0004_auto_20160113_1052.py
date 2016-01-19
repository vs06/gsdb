# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gospelsongsdb', '0003_auto_20160113_1045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musica',
            name='cultos',
        ),
        migrations.AddField(
            model_name='culto',
            name='musicas',
            field=models.ManyToManyField(db_column='musicas', to='gospelsongsdb.Musica'),
        ),
    ]
