# Generated by Django 3.2.9 on 2021-11-24 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('clave', models.CharField(max_length=5, unique=True)),
                ('departamento', models.CharField(max_length=100)),
                ('campus', models.CharField(max_length=100)),
            ],
        ),
    ]
