# Generated by Django 3.1.7 on 2021-03-31 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_app', '0003_remove_anime_episode'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='cover_image',
            field=models.URLField(default='https://upload.wikimedia.org/wikipedia/en/b/bd/Doraemon_character.png', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='anime',
            name='genres',
            field=models.CharField(default='Anime', max_length=255),
            preserve_default=False,
        ),
    ]
