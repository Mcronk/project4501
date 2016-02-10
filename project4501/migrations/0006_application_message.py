# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project4501', '0005_auto_20160208_0608'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('application_id', models.IntegerField(primary_key=True, serialize=False)),
                ('price', models.IntegerField(default=-1)),
                ('content', models.TextField(blank=True)),
                ('course', models.ForeignKey(to='project4501.Course')),
                ('student', models.ForeignKey(related_name='applicationstudent', to='project4501.User')),
                ('tutor', models.ForeignKey(related_name='applicationtutor', to='project4501.User')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('message_id', models.IntegerField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('receiver', models.ForeignKey(related_name='mreceiver', to='project4501.User')),
                ('sender', models.ForeignKey(related_name='msender', to='project4501.User')),
            ],
        ),
    ]
