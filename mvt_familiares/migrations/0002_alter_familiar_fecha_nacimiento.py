# Generated by Django 4.0.4 on 2022-05-17 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvt_familiares', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiar',
            name='fecha_nacimiento',
            field=models.CharField(max_length=10),
        ),
    ]
