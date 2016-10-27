# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-01 20:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelatedObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_id', models.IntegerField(db_index=True)),
                ('object_id', models.IntegerField(db_index=True)),
                ('alias', models.CharField(blank=True, max_length=255)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('object_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_relatedobject', to='contenttypes.ContentType')),
                ('parent_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_relatedobject', to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ('-creation_date',),
            },
        ),
    ]