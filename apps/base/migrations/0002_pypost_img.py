# Generated by Django 2.2.4 on 2019-09-16 23:27

import apps.base.models.post
import apps.base.rename_image
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pypost',
            name='img',
            field=models.ImageField(blank=True, default='post/default_post.png', max_length=255, null=True, storage=apps.base.rename_image.RenameImage(), upload_to=apps.base.models.post.image_path),
        ),
    ]