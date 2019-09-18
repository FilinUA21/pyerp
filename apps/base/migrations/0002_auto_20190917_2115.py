# Generated by Django 2.2.4 on 2019-09-18 00:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pyparameter',
            name='name',
            field=models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-z]*$', 'Only lowercase alphanumeric characters are allowed.')], verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='pyparameter',
            name='value',
            field=models.CharField(max_length=255, verbose_name='Value'),
        ),
    ]