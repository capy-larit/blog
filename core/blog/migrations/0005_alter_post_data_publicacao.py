# Generated by Django 4.1.1 on 2022-10-05 14:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_data_publicacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 10, 5, 14, 6, 7, 383886, tzinfo=datetime.timezone.utc)),
        ),
    ]
