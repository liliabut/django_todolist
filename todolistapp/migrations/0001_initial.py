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
                ('title', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=200)),
                ('prio', models.CharField(max_length=20)),
                ('progress', models.IntegerField(default=0)),
                ('status', models.CharField(default=b'Neu', max_length=200)),
                ('start_date', models.DateTimeField(verbose_name=b'date published')),
                ('due_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
    ]
