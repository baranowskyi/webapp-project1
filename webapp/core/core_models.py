from django.contrib.auth import get_user_model
from django.db import models

from django.core.validators import FileExtensionValidator, EmailValidator

#modifided slug for english and russian words
from pytils.translit import slugify


User = get_user_model()


class User(models.Model):
    login = models.CharField('Login', max_length=50, null=False, unique=True)
    password = models.CharField('Password', max_length=50, null=False, unique=True)
    email = models.EmailField('Email', max_length=50, null=False, unique=True, validators=[EmailValidator(message="Invalid Email")])
    pro_user = models.BooleanField("Pro User", default=False, editable=False)   
     
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ('id',)

    def __str__(self):        
        return f"{self.login}"
 
# def get_upload_path(instance, filename):
#    return f'{instance.Artist.display_name}'

# @staticmethod
# def get_url():
#     url = UserSite.login
#     return f'{url}'  
   
class Artist(models.Model):    
    display_name = models.CharField("Artist Name", max_length=100, null=True, blank=True)
    slug_artist = models.SlugField("Slug Artist", max_length=100, null=True, editable=False, unique=True)   
    profile_url = models.URLField("Profile URL", default="", null=False, unique=True)
    avatar_link = models.ImageField("Avatar", upload_to="", default="media/site/default_logo.png", blank=True)
    verification = models.BooleanField("Verification", default=False, editable=False)
    first_name = models.CharField("First Name", max_length=30, null=True, blank=True)
    last_name = models.CharField("Last Name", max_length=30, null=True, blank=True)
    city = models.CharField("City", max_length=30, null=True, blank=True)
    country = models.CharField("Country", max_length=30, null=True, blank=True)
    bio = models.TextField("Bio", max_length=500, null=True, blank=True)
    #social_network =
    user = models.OneToOneField('core.User', models.CASCADE, related_name='artist')
    
    # def save(self, *args, **kwargs):        
    #     if not self.display_name:                
    #         self.slug_artist = self.email.split('@')[0]
    #     else:    
    #         self.slug_artist = slugify(self.display_name)
    #     super(Artist, self).save(*args, **kwargs)    

    class Meta:
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'
        ordering = ('id',)

    def __str__(self):        
        return f"{self.display_name}"
    
    
class Track(models.Model):
    title = models.CharField("Title", max_length=255, blank=True)
    slug_track = models.SlugField("Slug Title", max_length=255, editable=False, unique=True)
    file_link = models.FileField("File", upload_to="user", null=False, validators=[FileExtensionValidator(allowed_extensions=['mp3', 'wav'])],)
    cover_link = models.ImageField("Cover", upload_to="user", default="site/default_logo.png", null=True, blank=True)
    genre = models.CharField("Genre", max_length=30, null=True, blank=True)
    tag = models.CharField("Tag", max_length=200, null=True, blank=True)
    public_access = models.BooleanField("Public Access", default=False)
    publish_date = models.DateTimeField("Published Date", auto_now_add=True)
    update_date = models.DateTimeField("Update Date", auto_now=True)
    discription = models.TextField("Discription", max_length=2000, null=True, blank=True)
    #like = models.BooleanField("Like", default=False, editable=False)
    #repost = models.BooleanField("Repost", default=False, editable=False)
    #share =
    copy_link = models.URLField("Copy Link", default="", editable=False)
    download_access = models.BooleanField("Download Access", default=False)
    buy_link = models.URLField("Buy Link", null=True, blank=True)
    play_counter = models.PositiveIntegerField("Play Counter", default=0, editable=False)
    like_counter = models.PositiveIntegerField("Like Counter", default=0, editable=False)
    repost_counter = models.PositiveIntegerField("Repost Counter", default=0, editable=False)
    comment_counter = models.PositiveIntegerField("Comment Counter", default=0, editable=False)
    artist = models.ForeignKey('core.Artist', models.CASCADE, related_name='tracks')
    
    def save(self, *args, **kwargs):        
        if not self.title:
            self.title = str(self.file_link)[:-4]
            self.slug_track = slugify(self.file_link)[:-3]            
        else:    
            self.slug_track = slugify(self.title)
        super(Track, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Track'
        verbose_name_plural = 'Tracks'
        ordering = ('id',)

    def __str__(self):        
        return f"{self.title}"
    
    
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
    
class Profile(models.Model):
    follower_counter = models.PositiveIntegerField("Follower Counter", default=0, editable=False)
    following_counter = models.PositiveIntegerField("Following Counter", default=0, editable=False)
    track_counter = models.PositiveIntegerField("Track Counter", default=0, editable=False)
    like_counter = models.PositiveIntegerField("Like Counter", default=0, editable=False)
    header_link = models.FileField("Header Cover", upload_to="user", default="site/default_logo.png", null=True, blank=True)
    artist = models.OneToOneField('core.Artist', models.CASCADE, related_name='profile')

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'
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
