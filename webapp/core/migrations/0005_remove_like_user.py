# Generated by Django 4.2.2 on 2023-07-18 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_like_user_alter_like_track'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
    ]
