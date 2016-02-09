# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project4501', '0004_auto_20160207_2108'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionInfo',
            fields=[
                ('info_id', models.IntegerField(serialize=False, primary_key=True)),
                ('qualification', models.CharField(max_length=30)),
                ('available_time', models.DateTimeField(verbose_name='Available Time')),
                ('price', models.IntegerField(default=-1)),
                ('course', models.ForeignKey(to='project4501.Course')),
                ('tutor', models.ForeignKey(to='project4501.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='strength',
            name='course',
        ),
        migrations.RemoveField(
            model_name='strength',
            name='tutor',
        ),
        migrations.RemoveField(
            model_name='session',
            name='price',
        ),
        migrations.DeleteModel(
            name='Strength',
        ),
    ]
