# Generated by Django 4.2.2 on 2023-07-12 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='profile_url',
            field=models.CharField(blank=True, unique=True, verbose_name='Profile URL'),
        ),
    ]
