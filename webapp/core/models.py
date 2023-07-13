from django.db import models

# validators
from django.core.validators import FileExtensionValidator

#modifided slug for english and russian words
from pytils.translit import slugify

# # signals
# from django.db.models.signals import post_save, pre_save
# from django.dispatch import receiver

# from users.models import UserSite

from core.service_functions import services

# from core.signals import *


class Artist(models.Model):    
    display_name = models.CharField("Artist Name", max_length=100, null=True, blank=True)
    slug_artist = models.SlugField("Slug Artist", max_length=100, null=True, unique=True)
    profile_url = models.CharField("Profile URL", null=False, unique=True, blank=True)
    avatar_image = models.ImageField("Avatar", 
                                    upload_to=services.get_avatar_upload_path,                                    
                                    null=True,
                                    blank=True,
                                    validators=[
                                    FileExtensionValidator(allowed_extensions=['jpg', 'png', 'gif']), 
                                    services.validate_size_avatar
                                    ]
                                    )
    header_image = models.ImageField("Header Cover", 
                                    upload_to=services.get_profile_headear_path,                                  
                                    null=True, 
                                    blank=True, 
                                    validators=[
                                    FileExtensionValidator(allowed_extensions=['jpg', 'png', 'gif']), 
                                    services.validate_size_profile_headear
                                    ]
                                    )
    verification = models.BooleanField("Verification", default=False)
    first_name = models.CharField("First Name", max_length=30, null=True, blank=True)
    last_name = models.CharField("Last Name", max_length=30, null=True, blank=True)
    city = models.CharField("City", max_length=30, null=True, blank=True)
    country = models.CharField("Country", max_length=30, null=True, blank=True)
    bio = models.TextField("Bio", max_length=500, null=True, blank=True)
    follower_counter = models.PositiveIntegerField("Follower Counter", default=0, editable=False)
    following_counter = models.PositiveIntegerField("Following Counter", default=0, editable=False)
    track_counter = models.PositiveIntegerField("Track Counter", default=0, editable=False)
    username = models.OneToOneField('users.UserSite', models.CASCADE)    

    class Meta:
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'
        ordering = ('id',)

    def __str__(self):        
        return f"{self.display_name}"  

    # def save(self, *args, **kwargs):        
    #     services.get_default_artist_profile_url(self) # get profile url       
    #     super(Artist, self).save(*args, **kwargs) 


    
class Track(models.Model):
    title = models.CharField("Title", max_length=255, blank=True)
    slug_track = models.SlugField("Slug Title", max_length=255, editable=False)
    track_file = models.FileField("File", upload_to=services.get_track_upload_path, null=False, 
                                    validators=[
                                    FileExtensionValidator(allowed_extensions=['mp3', 'wav']), 
                                    services.validate_size_track
                                    ]
                                 )
    cover_image = models.ImageField("Cover", upload_to="user", default="default_logo_artist.png", null=True, blank=True)
    genre = models.CharField("Genre", max_length=30, null=True, blank=True)
    tag = models.CharField("Tag", max_length=200, null=True, blank=True)
    public_access = models.BooleanField("Public Access", default=False)
    publish_date = models.DateTimeField("Published Date", auto_now_add=True)
    update_date = models.DateTimeField("Update Date", auto_now=True)
    discription = models.TextField("Discription", max_length=2000, null=True, blank=True)    
    copy_link = models.URLField("Copy Link", default="", editable=False)
    download_access = models.BooleanField("Download Access", default=False)
    buy_link = models.URLField("Buy Link", null=True, blank=True)
    play_counter = models.PositiveIntegerField("Play Counter", default=0, editable=False)
    like_counter = models.PositiveIntegerField("Like Counter", default=0, editable=False)
    repost_counter = models.PositiveIntegerField("Repost Counter", default=0, editable=False)
    comment_counter = models.PositiveIntegerField("Comment Counter", default=0, editable=False)
    artist = models.ForeignKey('core.Artist', models.CASCADE)
    
    class Meta:
        verbose_name = 'Track'
        verbose_name_plural = 'Tracks'
        ordering = ('id',)

    def __str__(self):        
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        services.get_slug_track_and_name(self)
        super(Track, self).save(*args, **kwargs)    
    
    
class Comment(models.Model):
    date = models.DateTimeField("Date", auto_now_add=True, editable=False)
    comment = models.TextField("Comment", max_length=2000, null=False, blank=False)
    track = models.ForeignKey('core.Track', models.CASCADE)
    artist = models.ForeignKey('core.Artist', models.CASCADE)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ('id',)

    def __str__(self):        
        return f"id {self.pk}"

    
class Like(models.Model):
    like = models.BooleanField("Like", default=False)
    track = models.ForeignKey('core.Track', models.CASCADE)
    artist = models.ForeignKey('core.Artist', models.CASCADE)

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
        ordering = ('id',)

    def __str__(self):        
        return f"id {self.pk}"
    
    
class SocialNetwork(models.Model):
    name = models.CharField('Social Network', max_length=50)
    url = models.URLField("Profile URL", max_length=200)
    artist = models.ForeignKey('core.Artist', models.CASCADE)

    class Meta:
        verbose_name = 'Social Network'
        verbose_name_plural = 'Social Networks'
        ordering = ('id',)

    def __str__(self):        
        return f"id {self.pk}"
    

class Repost(models.Model):
    repost = models.BooleanField("Repost", default=False)
    track = models.ForeignKey('core.Track', models.CASCADE)
    artist = models.ForeignKey('core.Artist', models.CASCADE)

    class Meta:
        verbose_name = 'Repost'
        verbose_name_plural = 'Reposts'
        ordering = ('id',)

    def __str__(self):        
        return f"id {self.pk}"
