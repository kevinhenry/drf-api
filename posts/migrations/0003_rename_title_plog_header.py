# Generated by Django 3.2.7 on 2021-09-09 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_rename_headline_plog_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plog',
            old_name='title',
            new_name='header',
        ),
    ]