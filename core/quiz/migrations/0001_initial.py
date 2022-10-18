# Generated by Django 4.1.1 on 2022-10-18 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enunciado', models.TextField(default='', max_length=255)),
                ('imagem', models.ImageField(blank=True, default='', null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Alternativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(default='', max_length=255)),
                ('isCorreta', models.BooleanField(blank=True, default=False, null=True)),
                ('questao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.questao')),
            ],
        ),
    ]
