# Generated by Django 2.2.1 on 2019-08-27 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_is_favourite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='is_favourite',
            new_name='is_favorite',
        ),
    ]
