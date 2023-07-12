# Generated by Django 4.2.2 on 2023-07-12 13:18

import core.service_functions.services
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_artist_profile_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='avatar_link',
            field=models.ImageField(blank=True, null=True, upload_to=core.service_functions.services.get_avatar_upload_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'gif']), core.service_functions.services.validate_size_avatar], verbose_name='Avatar'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='header_link',
            field=models.ImageField(blank=True, null=True, upload_to=core.service_functions.services.get_profile_background_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'gif']), core.service_functions.services.validate_size_profile_background], verbose_name='Header Cover'),
        ),
        migrations.AlterField(
            model_name='track',
            name='cover_link',
            field=models.ImageField(blank=True, default='site/logo_artist.png', null=True, upload_to='user', verbose_name='Cover'),
        ),
    ]