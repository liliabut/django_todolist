# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('beschreibung', models.CharField(max_length=200)),
                ('status', models.CharField(default=b'Normal', max_length=20)),
                ('fortschritt', models.IntegerField(default=0)),
                ('start', models.DateTimeField(verbose_name=b'start')),
                ('frist', models.DateTimeField(verbose_name=b'frist')),
            ],
        ),
    ]
