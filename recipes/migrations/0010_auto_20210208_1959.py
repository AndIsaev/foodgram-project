# Generated by Django 2.2 on 2021-02-08 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_auto_20210208_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=models.CharField(max_length=15, verbose_name='Цвет тега'),
        ),
    ]