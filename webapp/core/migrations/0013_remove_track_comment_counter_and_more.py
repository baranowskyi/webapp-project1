# Generated by Django 4.2.2 on 2023-07-23 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_remove_like_username_like_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='comment_counter',
        ),
        migrations.RemoveField(
            model_name='track',
            name='like_counter',
        ),
        migrations.RemoveField(
            model_name='track',
            name='play_counter',
        ),
        migrations.RemoveField(
            model_name='track',
            name='repost_counter',
        ),
    ]