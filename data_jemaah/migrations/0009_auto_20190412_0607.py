# Generated by Django 2.1.2 on 2019-04-11 23:07

import data_jemaah.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_jemaah', '0008_auto_20190411_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jemaah_umroh',
            name='foto',
            field=models.ImageField(blank=True, default='tidak_ada.jpg', null=True, upload_to=data_jemaah.models.path_and_rename),
        ),
    ]