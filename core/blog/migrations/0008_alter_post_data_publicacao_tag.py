# Generated by Django 4.1.1 on 2022-10-19 12:50

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_post_conteudo_remove_post_resumo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(
                verbose_name=datetime.datetime(
                    2022,
                    10,
                    19,
                    12,
                    50,
                    23,
                    12824,
                    tzinfo=datetime.timezone.utc,
                )
            ),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('nome', models.CharField(max_length=50)),
                ('posts', models.ManyToManyField(to='blog.post')),
            ],
        ),
    ]
