# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-06 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_delete_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='auther',
        ),
        migrations.AddField(
            model_name='contact',
            name='context',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='post_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='contact',
            name='time',
            field=models.CharField(default=454, max_length=25),
            preserve_default=False,
        ),
    ]
