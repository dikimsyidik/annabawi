# Generated by Django 2.1.2 on 2019-04-10 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_jemaah', '0004_auto_20190410_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jemaah_umroh',
            name='rombongan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data_jemaah.Umroh'),
        ),
    ]
