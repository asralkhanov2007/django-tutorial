# Generated by Django 3.2.2 on 2021-05-27 13:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=datetime.datetime(2021, 5, 27, 13, 29, 24, 751797, tzinfo=utc), upload_to='posters/', verbose_name='Poster'),
            preserve_default=False,
        ),
    ]
