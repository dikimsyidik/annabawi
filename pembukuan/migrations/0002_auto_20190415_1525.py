# Generated by Django 2.1.2 on 2019-04-15 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pembukuan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atk',
            name='tanggal_input',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='handling',
            name='tanggal_input',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='kendaraan',
            name='tanggal_input',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='la',
            name='tanggal_input',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='paspor',
            name='tanggal_input',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='pembukuan_haji',
            name='tanggal_input',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='pembukuan_honor_karyawan',
            name='tanggal_input',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='pembukuan_pajak',
            name='tanggal_input',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='pembukuan_umroh',
            name='tanggal_input',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='tiket',
            name='tanggal_input',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='transfortasi',
            name='tanggal_input',
            field=models.DateTimeField(),
        ),
    ]
