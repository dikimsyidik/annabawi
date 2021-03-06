# Generated by Django 2.1.2 on 2019-04-09 14:01

import data_jemaah.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Haji',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pemberangkatan', models.CharField(max_length=100)),
                ('harga', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Jemaah_Hajis',
            fields=[
                ('id', models.CharField(default=data_jemaah.models.create_id, max_length=100, primary_key=True, serialize=False)),
                ('nama_lengkap', models.CharField(max_length=200)),
                ('foto', models.ImageField(upload_to='')),
                ('alamat', models.TextField()),
                ('tempat_lahir', models.CharField(max_length=100)),
                ('tanggal_lahir', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('tunggakan', models.IntegerField(blank=True, null=True)),
                ('rombongan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rombongan', to='data_jemaah.Haji')),
            ],
        ),
    ]
