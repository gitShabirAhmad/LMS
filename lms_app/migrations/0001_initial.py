# Generated by Django 4.2.4 on 2023-11-05 16:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('time', models.CharField(max_length=45)),
                ('started_date', models.DateField()),
                ('students', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]