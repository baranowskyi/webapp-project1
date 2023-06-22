from django.db import models

from django.core.validators import FileExtensionValidator

#slug english + cirilic
from pytils.translit import slugify


class Artist(models.Model):   
    """
    Conteined main information about an artist 
    """ 
    login = models.CharField("Login", max_length=30, null=False, unique=True)
    password = models.CharField("Password", max_length=50, null=False, unique=True)
    email = models.CharField("Email", max_length=30, null=False, unique=True)
    date_registration = models.DateTimeField("Date Registration", auto_now_add=True)
    artist_display_name = models.CharField("Artist Name", max_length=100, null=False)
    slug_artist = models.SlugField("Slug Artist", max_length=100, editable=False, unique=True)
    avatar_link = models.FileField("Avatar", upload_to="static/media/user", default="static/media/site/default_logo.png", blank=True)
    profile_url = models.URLField("Profile URL", default="", unique=True, null=False)
    first_name = models.CharField("First Name", max_length=30, null=True, blank=True)
    last_name = models.CharField("Last Name", max_length=30, null=True, blank=True)
    city = models.CharField("City", max_length=30, null=True, blank=True)
    country = models.CharField("Country", max_length=30, null=True, blank=True)
    bio = models.TextField("Bio", max_length=500, null=True, blank=True)
    #social_network =
    verification = models.BooleanField("Verification", default=False, editable=False)  
    pro_user = models.BooleanField("Pro User", default=False, editable=False)  

    def save(self, *args, **kwargs):
        if not self.slug_artist:
            self.slug_artist = slugify(self.artist_display_name)
        super(Artist, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.artist_display_name}"
    

class SocialNetwork(models.Model):
    name = models.CharField("Name", max_length=100, null=True, blank=True)
    link = models.URLField("Link", null=True, blank=True)    


class Track(models.Model):
    title = models.CharField("Title", max_length=255, null=False)
    slug_title = models.SlugField("Slug Title", max_length=255, editable=False, unique=True)
    file_link = models.FileField("File", upload_to="static/media/user", null=False, validators=[FileExtensionValidator(allowed_extensions=['mp3', 'wav'])],)
    cover_link = models.FileField("Cover", upload_to="static/media/user", default="static/media/site/default_logo.png", null=True, blank=True)
    genre = models.CharField("Genre", max_length=100, null=True, blank=True)
    tag = models.CharField("Tag", max_length=100, null=True, blank=True)
    public_access = models.BooleanField("Public Access", default=False)
    publish_date = models.DateTimeField("Published Date", auto_now_add=True)
    update_date = models.DateTimeField("Update Date", auto_now=True)
    discription = models.TextField("Discription", max_length=2000, null=True, blank=True)
    #like = models.BooleanField("Like", default=False, editable=False)
    #repost = models.BooleanField("Repost", default=False, editable=False)
    #share =
    #copy_link =
    download_access = models.BooleanField("Download Access", default=False)
    buy_link = models.URLField("Buy Link", null=True, blank=True)
    play_counter = models.PositiveIntegerField("Play Counter", default=0, null=True, editable=False)
    like_counter = models.PositiveIntegerField("Like Counter", default=0, null=True, editable=False)
    repost_counter = models.PositiveIntegerField("Repost Counter", default=0, null=True, editable=False)
    comment_counter = models.PositiveIntegerField("Comment Counter", default=0, null=True,editable=False)

    def save(self, *args, **kwargs):
        if not self.slug_title:
            self.slug_title = slugify(self.title)
        super(Track, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"