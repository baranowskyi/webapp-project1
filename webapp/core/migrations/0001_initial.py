# Generated by Django 4.2.2 on 2023-06-22 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=30, unique=True, verbose_name='Login')),
                ('password', models.CharField(max_length=50, unique=True, verbose_name='Password')),
                ('email', models.CharField(max_length=30, unique=True, verbose_name='Email')),
                ('date_registration', models.DateTimeField(auto_now_add=True, verbose_name='Date Registration')),
                ('artist_display_name', models.CharField(max_length=100, verbose_name='Artist Name')),
                ('slug_artist', models.SlugField(editable=False, max_length=100, verbose_name='Slug')),
                ('avatar_link', models.FileField(blank=True, default='static/media/site/default_logo.png', upload_to='static/media/user', verbose_name='Avatar')),
                ('profile_url', models.URLField(default='', unique=True, verbose_name='Profile URL')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Last Name')),
                ('city', models.CharField(blank=True, max_length=30, null=True, verbose_name='City')),
                ('country', models.CharField(blank=True, max_length=30, null=True, verbose_name='Country')),
                ('bio', models.TextField(blank=True, max_length=500, null=True, verbose_name='Bio')),
                ('verification', models.BooleanField(default=False, editable=False, verbose_name='Verification')),
                ('pro_user', models.BooleanField(default=False, editable=False, verbose_name='Pro User')),
            ],
        ),
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Link')),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('slug_title', models.SlugField(editable=False, max_length=100, verbose_name='Slug Title')),
                ('file_link', models.FileField(upload_to='static/media/user', verbose_name='File')),
                ('cover_link', models.FileField(blank=True, default='static/media/site/default_logo.png', null=True, upload_to='static/media/user', verbose_name='Cover')),
                ('genre', models.CharField(blank=True, max_length=100, null=True, verbose_name='Genre')),
                ('tag', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tag')),
                ('public_access', models.BooleanField(default=False, verbose_name='Public Access')),
                ('publish_date', models.DateTimeField(auto_now_add=True, verbose_name='Published Date')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Update Date')),
                ('discription', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Discription')),
                ('like', models.BooleanField(default=False, editable=False, verbose_name='Like')),
                ('repost', models.BooleanField(default=False, editable=False, verbose_name='Repost')),
                ('download_access', models.BooleanField(default=False, verbose_name='Download Access')),
                ('buy_link', models.URLField(blank=True, null=True, verbose_name='Buy Link')),
                ('play_counter', models.PositiveIntegerField(default=None, editable=False, verbose_name='Play Counter')),
                ('like_counter', models.PositiveIntegerField(default=None, editable=False, verbose_name='Like Counter')),
                ('repost_counter', models.PositiveIntegerField(default=None, editable=False, verbose_name='Repost Counter')),
                ('comment_counter', models.PositiveIntegerField(default=None, editable=False, verbose_name='Comment Counter')),
            ],
        ),
    ]
