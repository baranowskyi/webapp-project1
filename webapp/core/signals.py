from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from core.models import Artist
from users.models import UserSite
from core.service_functions import services

import os

from core.service_functions import constants
from django.conf import settings

# create artist data after create user 
@receiver(post_save, sender=UserSite)
def create_artist(sender, instance, created, **kwargs):        
    if created:            
        Artist.objects.create(
            username=instance, 
            slug_artist=services.get_default_slug_artist(),
            display_name=services.get_default_slug_artist(),
            avatar_image=services.get_default_avatar_image(),
            header_image=services.get_default_header_image(),
            profile_url=services.get_default_artist_profile_url()
            )  


# delete old image (avatar, background) file after replace
@receiver(pre_save, sender=Artist)
def save_image(sender, instance, *args, **kwargs): 

    default_avatar = f"{settings.MEDIA_ROOT}\{constants.DEFAULT_AVATAR}"
    default_header = f"{settings.MEDIA_ROOT}\{constants.DEFAULT_HEADER}"
    
    try: 
        old_img_avatar = instance.__class__.objects.get(id=instance.id).avatar_image.path         
        try:
            new_img_avatar = instance.avatar_image.path            
        except:
            new_img_avatar = None
        if new_img_avatar != old_img_avatar:            
            if (os.path.exists(old_img_avatar)) and (old_img_avatar != default_avatar):
                os.remove(old_img_avatar)
    except:
        pass

    try:
        old_img_header = instance.__class__.objects.get(id=instance.id).header_image.path        
        try:
            new_img_header = instance.header_image.path            
        except:
            new_img_header = None
        if new_img_header != old_img_header:            
            if (os.path.exists(old_img_header)) and (old_img_header != default_header):
                os.remove(old_img_header)
    except:
        pass


