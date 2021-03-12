# Generated by Django 2.2 on 2021-03-12 05:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0021_auto_20210310_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quantity',
            name='amount',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Количество'),
        ),
    ]
