# Generated by Django 4.2.4 on 2023-11-06 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cls',
            name='started_date',
            field=models.DateField(default='2023-11-6'),
        ),
    ]
