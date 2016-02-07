# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('class_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.IntegerField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('course', models.ForeignKey(to='project4501.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('session_id', models.IntegerField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(verbose_name='Class Time')),
                ('price', models.IntegerField()),
                ('course', models.ForeignKey(to='project4501.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Strength',
            fields=[
                ('strength_id', models.IntegerField(primary_key=True, serialize=False)),
                ('qualification', models.CharField(max_length=30)),
                ('course', models.ForeignKey(to='project4501.Course')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('phone', models.IntegerField()),
                ('description', models.TextField()),
                ('grade', models.IntegerField(default=0)),
                ('courses', models.ManyToManyField(blank=True, to='project4501.Course', related_name='users')),
            ],
        ),
        migrations.AddField(
            model_name='strength',
            name='tutor',
            field=models.ForeignKey(to='project4501.User'),
        ),
        migrations.AddField(
            model_name='session',
            name='student',
            field=models.ForeignKey(related_name='student', to='project4501.User'),
        ),
        migrations.AddField(
            model_name='session',
            name='tutor',
            field=models.ForeignKey(related_name='tutor', to='project4501.User'),
        ),
        migrations.AddField(
            model_name='review',
            name='receiver',
            field=models.ForeignKey(related_name='receiver', to='project4501.User'),
        ),
        migrations.AddField(
            model_name='review',
            name='writer',
            field=models.ForeignKey(related_name='writter', to='project4501.User'),
        ),
    ]
