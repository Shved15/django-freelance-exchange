# Generated by Django 4.0 on 2023-04-22 11:36

import allapps.user.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allapps_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=allapps.user.models.user_directory_path),
        ),
    ]