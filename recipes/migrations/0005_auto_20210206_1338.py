# Generated by Django 2.2 on 2021-02-06 10:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20210128_1228'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'тег', 'verbose_name_plural': 'теги'},
        ),
        migrations.RemoveField(
            model_name='tag',
            name='tag',
        ),
        migrations.AddField(
            model_name='tag',
            name='display_name',
            field=models.CharField(default=datetime.datetime(2021, 2, 6, 10, 38, 26, 938626, tzinfo=utc), max_length=60, verbose_name='Имя тега для шаблона'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='title',
            field=models.CharField(db_index=True, default=datetime.datetime(2021, 2, 6, 10, 38, 31, 132626, tzinfo=utc), max_length=60, verbose_name='Имя тега'),
            preserve_default=False,
        ),
    ]