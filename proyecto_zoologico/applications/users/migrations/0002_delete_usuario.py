# Generated by Django 3.1.5 on 2021-01-24 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animales', '0002_auto_20210124_1536'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
