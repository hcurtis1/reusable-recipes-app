# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_blog', '0005_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cooking_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='diet_info',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='difficulty',
            field=models.CharField(choices=[(b'Simple', 'SIMPLE'), (b'Not too hard', 'NOT TOO HARD'), (b'Tricky', 'TRICKY')], default='Simple', max_length=15),
        ),
        migrations.AddField(
            model_name='post',
            name='serves',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1),
        ),
    ]