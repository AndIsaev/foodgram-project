# Generated by Django 2.2 on 2021-03-10 12:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0019_auto_20210310_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='dimension',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Мера'),
        ),
    ]
