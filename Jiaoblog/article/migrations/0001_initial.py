# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '\u6587\u7ae0',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '\u6807\u7b7e',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ForeignKey(to='article.Tags'),
        ),
    ]
