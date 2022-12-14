# Generated by Django 4.1.1 on 2022-10-19 14:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            'contas',
            '0002_remove_perfil_id_alter_perfil_foto_alter_perfil_user',
        ),
        (
            'blog',
            '0010_postsituacao_alter_post_data_publicacao_situacao_and_more',
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateField(),
        ),
        migrations.CreateModel(
            name='Comentario',
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
                ('texto', models.TextField(max_length=1024)),
                (
                    'perfil',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to='contas.perfil',
                    ),
                ),
                (
                    'post',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='blog.post',
                    ),
                ),
            ],
        ),
    ]
