# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project4501', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='popularity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='course',
            name='tag',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(blank=True),
        ),
    ]
