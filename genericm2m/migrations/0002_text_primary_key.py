# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-04 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genericm2m', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relatedobject',
            name='object_id',
            field=models.TextField(db_index=True),
        ),
        migrations.AlterField(
            model_name='relatedobject',
            name='parent_id',
            field=models.TextField(db_index=True),
        ),
    ]