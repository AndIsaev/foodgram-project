# Generated by Django 2.2 on 2021-03-10 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0017_auto_20210308_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
    ]
