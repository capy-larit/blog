# Generated by Django 4.1.1 on 2022-10-05 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assunto', models.CharField(choices=[('', 'Selecione um assunto'), ('descontos', 'Descontos'), ('consultoria', 'Consultoria'), ('freelance', 'Freelance'), ('elogios', 'Elogios'), ('reclamações', 'Reclamações'), ('outros', 'Outros')], default='', max_length=100)),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('mensagem', models.TextField(max_length=1000)),
            ],
        ),
    ]
