# Generated by Django 3.1.3 on 2020-11-23 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0004_auto_20201120_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='libros', to='libros.autor'),
        ),
    ]