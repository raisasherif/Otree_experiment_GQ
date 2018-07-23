# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-07-23 11:53
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_player_total_correct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='total_correct',
            field=otree.db.models.IntegerField(default=0, null=True),
        ),
    ]