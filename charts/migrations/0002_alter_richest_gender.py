# Generated by Django 4.1.7 on 2023-08-01 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='richest',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
    ]
