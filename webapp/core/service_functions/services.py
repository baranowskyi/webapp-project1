from django.core.exceptions import ValidationError

import absoluteuri

from core.service_functions import constants

#modifided slug for english and russian words
from pytils.translit import slugify

############################
######### UPLOAD FILE
############################

### avatar 

def get_avatar_upload_path(instance, file):
    # media/user/user_id/avatar
    return f"artist/artist_{instance.profile}/avatar/{file}"

def validate_size_avatar(file):    
    if file.size > constants.AVATAR_SIZE_LIMIT * (1024 ** 2):
        raise ValidationError(f"Upload File {file.size/1024/1024} MB > File Limit {constants.AVATAR_SIZE_LIMIT} MB")
    

### track 
    
def get_track_upload_path(instance, file):
    # media/user/user_id/track
    return f"artist/artist_{instance.profile}/track/{file}"
    
def validate_size_track(file):    
    if file.size > constants.TRACK_SIZE_LIMIT * (1024 ** 2):        
        raise ValidationError(f"Upload File {file.size/1024/1024} MB > File Limit {constants.TRACK_SIZE_LIMIT} MB")
    

### profile background    
    
def get_profile_background_path(instance, file):
    # media/user/user_id/background
    return f"artist/artist_{instance.profile}/background/{file}"
    
def validate_size_profile_background(file):
    if file.size > constants.BACKGROUND_SIZE_LIMIT * (1024 ** 2):        
        raise ValidationError(f"Upload File {file.size/1024/1024} MB > File Limit {constants.BACKGROUND_SIZE_LIMIT} MB")


############################
######### GENERATE URL
############################

### slug track and name

def get_slug_track_and_name(instance):                
        if not instance.title:
            instance.title = str(instance.file_link)[:-4] 
            instance.slug_track = slugify(instance.file_link)[:-3]            
        else:    
            instance.slug_track = slugify(instance.title)
        return instance



### slug artist

### url artist profile

def get_artist_profile_url(instance):
    instance.profile_url = absoluteuri.build_absolute_uri(f"/{instance.slug_artist}")
    return instance
