# Generated by Django 2.1.2 on 2019-04-11 11:26

import data_jemaah.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_jemaah', '0007_auto_20190411_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jemaah_hajis',
            name='foto',
            field=models.ImageField(blank=True, default='tidak_ada.jpg', null=True, upload_to=data_jemaah.models.path_and_rename),
        ),
        migrations.AlterField(
            model_name='jemaah_hajis',
            name='tanggal_lahir',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='jemaah_hajis',
            name='tempat_lahir',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='jemaah_umroh',
            name='tanggal_lahir',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='jemaah_umroh',
            name='tempat_lahir',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
