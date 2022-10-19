# Generated by Django 4.1.1 on 2022-10-19 12:53

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_data_publicacao_tag'),
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
                    53,
                    47,
                    236200,
                    tzinfo=datetime.timezone.utc,
                )
            ),
        ),
        migrations.CreateModel(
            name='Assunto',
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
                ('nome', models.CharField(max_length=255)),
                ('posts', models.ManyToManyField(to='blog.post')),
            ],
        ),
    ]