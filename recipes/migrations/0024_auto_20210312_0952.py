# Generated by Django 2.2 on 2021-03-12 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0023_auto_20210312_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Названи'),
        ),
    ]
