from django.core.exceptions import ValidationError

from core.service_functions import constants

# modifided slug for english and russian words
from pytils.translit import slugify

from users.models import UserSite

from PIL import Image

#--------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------ UPLOAD FILE -------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------ avatar 

def get_default_avatar_image():      
    return f"{constants.DEFAULT_AVATAR}" 


def get_default_avatar_image_small():      
    return f"{constants.DEFAULT_AVATAR_SMALL}"


def get_avatar_upload_path(instance, file):
    # media/artist/username_[username]/avatar

    # resize and save user avatar for navbar avatar 
    img = Image.open(file)
    img_resize_lanczos = img.resize((200, 200), Image.LANCZOS)
    img_resize_lanczos.save(f"artist/username_{instance.username}/avatar/200x200_{file}")

    # return main user avatar
    return f"artist/username_{instance.username}/avatar/{file}"
    

def validate_size_avatar(file):    
    if file.size > constants.AVATAR_SIZE_LIMIT * (1024 ** 2):
        raise ValidationError(f"Upload File {file.size/1024/1024} MB > File Limit {constants.AVATAR_SIZE_LIMIT} MB")
    
 

    

#------------------------------------------------------------- profile header  
 
def get_default_header_image():      
    return f"{constants.DEFAULT_HEADER}"
 
    
def get_profile_headear_path(instance, file):
    # media/artist/username_[username]/header
    return f"artist/username_{instance.username}/header/{file}"
    
    
def validate_size_profile_headear(file):
    if file.size > constants.HEADER_SIZE_LIMIT * (1024 ** 2):        
        raise ValidationError(f"Upload File {file.size/1024/1024} MB > File Limit {constants.HEADER_SIZE_LIMIT} MB")
    
#-------------------------------------------------------------- cover

def get_default_cover_image():      
    return f"{constants.DEFAULT_COVER}"  
 

def get_cover_upload_path(instance, file):
    # media/artist/username_[username]/track
    return f"artist/username_{instance.artist.username}/track/{instance.slug_track}/{file}"
 

def validate_size_cover(file):    
    if file.size > constants.COVER_SIZE_LIMIT * (1024 ** 2):
        raise ValidationError(f"Upload File {file.size/1024/1024} MB > File Limit {constants.COVER_SIZE_LIMIT} MB")

#-------------------------------------------------------------- track 
    
def get_track_upload_path(instance, file):
    # media/artist/username_[username]/track  
    return f"artist/username_{instance.artist.username}/track/{instance.slug_track}/{file}"
    
def validate_size_track(file):    
    if file.size > constants.TRACK_SIZE_LIMIT * (1024 ** 2):        
        raise ValidationError(f"Upload File {file.size/1024/1024} MB > File Limit {constants.TRACK_SIZE_LIMIT} MB")  
    

#-------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------- GENERATE URL --------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------- slug track and name

def get_slug_track_and_name(instance):                
        if not instance.title:
            instance.title = str(instance.track_file)[:-4] 
            instance.slug_track = slugify(instance.track_file)[:-3]            
        else:    
            instance.slug_track = slugify(instance.title)
        return instance

#--------------------------------------------------------------- slug artist and name

# from email
# def get_default_slug_artist():
#     slug_artist = UserSite.objects.values().last()['email']
#     slug_artist = slugify(str(slug_artist).partition('@')[0])
#     return slug_artist

# from id user
def get_default_slug_artist_and_name():
    slug_artist = UserSite.objects.values().last()['id']
    name_artist = "User " + str(slug_artist)
    slug_artist = slugify("User " + str(slug_artist))    
    return {"slug_artist" : slug_artist, "name_artist" : name_artist}

#---------------------------------------------------------------- url artist profile

# def get_default_artist_profile_url(instance):   
#     instance.profile_url = f"{instance.slug_artist}"
#     return instance

# def get_default_artist_profile_url():   
#     profile_url = get_default_slug_artist_and_name()["slug_artist"]
#     return profile_url





  
