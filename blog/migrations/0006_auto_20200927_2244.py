# Generated by Django 3.1.1 on 2020-09-27 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200927_2244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpage',
            old_name='huina',
            new_name='author',
        ),
    ]
