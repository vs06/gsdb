# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gospelsongsdb', '0002_auto_20160112_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='culto',
            name='songs',
        ),
        migrations.AddField(
            model_name='musica',
            name='cultos',
            field=models.ManyToManyField(db_column='cultos', to='gospelsongsdb.Culto'),
        ),
    ]
