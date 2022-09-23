# Generated by Django 4.1.1 on 2022-09-23 19:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=255)),
                ('titulo', models.CharField(max_length=255)),
                ('subtitulo', models.CharField(max_length=255)),
                ('conteudo', models.TextField()),
                ('data_publicacao', models.DateTimeField(default=datetime.datetime(2022, 9, 23, 19, 31, 14, 408742))),
            ],
        ),
    ]
