# Generated by Django 3.1.1 on 2020-09-27 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogpage_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpage',
            old_name='author',
            new_name='huina',
        ),
    ]
