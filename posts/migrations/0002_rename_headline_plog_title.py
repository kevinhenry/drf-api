# Generated by Django 3.2.7 on 2021-09-09 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plog',
            old_name='headline',
            new_name='title',
        ),
    ]