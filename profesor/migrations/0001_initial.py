# Generated by Django 3.0 on 2019-12-17 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('carrera', models.CharField(max_length=50)),
                ('duracion', models.CharField(max_length=10)),
                ('especialidad', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'profesor',
            },
        ),
    ]
