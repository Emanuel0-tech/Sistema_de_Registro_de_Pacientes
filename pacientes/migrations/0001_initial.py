# Generated by Django 5.1.4 on 2025-01-16 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('data_nascimento', models.DateField()),
                ('historico_medico', models.TextField()),
            ],
        ),
    ]
