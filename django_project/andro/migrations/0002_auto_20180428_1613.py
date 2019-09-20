# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('andro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quiz_id', models.IntegerField(default=0, null=True, blank=True)),
                ('img', models.CharField(max_length=250)),
                ('catchphrase', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='score',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]
