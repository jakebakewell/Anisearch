# Generated by Django 3.1.7 on 2021-03-30 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime',
            name='link',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='studio',
        ),
        migrations.AddField(
            model_name='anime',
            name='anilist_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='anime',
            name='anilist_link',
            field=models.URLField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='anime',
            name='at_time',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='anime',
            name='episode',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='anime',
            name='filename',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='anime',
            name='from_time',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='anime',
            name='mal_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='anime',
            name='mal_link',
            field=models.URLField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='anime',
            name='to_time',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='anime',
            name='tokenthumb',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
