# Generated by Django 4.1.1 on 2022-10-19 12:42

import datetime

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_data_publicacao_topico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='conteudo',
        ),
        migrations.RemoveField(
            model_name='post',
            name='resumo',
        ),
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(
                verbose_name=datetime.datetime(
                    2022,
                    10,
                    19,
                    12,
                    42,
                    9,
                    641382,
                    tzinfo=datetime.timezone.utc,
                )
            ),
        ),
        migrations.AlterField(
            model_name='topico',
            name='conteudo',
            field=ckeditor_uploader.fields.RichTextUploadingField(
                blank=True, null=True
            ),
        ),
    ]
