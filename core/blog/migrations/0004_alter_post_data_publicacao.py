# Generated by Django 4.1.1 on 2022-10-05 14:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_imagem_capa_post_resumo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 10, 5, 14, 5, 45, 958147, tzinfo=datetime.timezone.utc)),
        ),
    ]