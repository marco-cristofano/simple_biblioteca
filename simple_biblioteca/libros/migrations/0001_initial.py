# Generated by Django 3.1.3 on 2020-11-20 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_fantasia', models.CharField(max_length=150)),
                ('nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('editorial', models.CharField(max_length=250)),
                ('fecha_publicacion', models.DateTimeField()),
                ('cantidad_paginas', models.PositiveIntegerField()),
                ('genero', models.CharField(choices=[('DR', 'Drama'), ('RO', 'Romantico'), ('IN', 'Infantil'), ('CF', 'Ciencia Ficcion'), ('OT', 'Otro')], default='OT', max_length=2)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='libros.autor')),
            ],
        ),
    ]