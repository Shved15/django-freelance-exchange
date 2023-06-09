# Generated by Django 4.0 on 2023-04-21 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('allapps_comment', '0001_initial'),
        ('allapps_offer', '0001_initial'),
        ('allapps_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allapps_user.user'),
        ),
        migrations.AddField(
            model_name='comment',
            name='offer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allapps_offer.offer'),
        ),
    ]
