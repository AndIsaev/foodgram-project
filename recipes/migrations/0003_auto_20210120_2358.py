# Generated by Django 2.2 on 2021-01-20 20:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20210119_1740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='key',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='value',
        ),
        migrations.AddField(
            model_name='tag',
            name='tag',
            field=models.CharField(default=datetime.datetime(2021, 1, 20, 20, 58, 4, 634616, tzinfo=utc), max_length=60, verbose_name='Тег'),
            preserve_default=False,
        ),
    ]