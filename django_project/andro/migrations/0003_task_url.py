# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('andro', '0002_auto_20180428_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='url',
            field=models.CharField(default=1, max_length=2500),
            preserve_default=False,
        ),
    ]
