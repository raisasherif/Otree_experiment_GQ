# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-07-24 10:52
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0003_auto_20180724_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='actual_1',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='actual_2',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='actual_3',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='actual_4',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='actual_5',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]
