# Generated by Django 2.2.4 on 2019-08-28 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0070_pypartner_not_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pypartner',
            name='not_email',
            field=models.BooleanField(default=False, verbose_name='No Email'),
        ),
    ]