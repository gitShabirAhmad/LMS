# Generated by Django 4.2.4 on 2023-11-11 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='address',
            field=models.CharField(default='Kabul', max_length=50),
        ),
    ]