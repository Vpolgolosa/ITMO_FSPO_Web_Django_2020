# Generated by Django 3.0.3 on 2020-03-10 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shar_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Owner',
        ),
    ]
