from django.db import models

from django.contrib.auth.models import AbstractUser

class UserSite(AbstractUser):
    username = models.CharField('User Name', max_length=50, null=False, unique=True)
    password = models.CharField('Password', max_length=255, null=False, unique=True)
    email = models.EmailField('Email', max_length=50, null=False, unique=True)
    pro_user = models.BooleanField("Pro User", default=False, editable=False)  
          
     
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ('id',)

    def __str__(self):        
        return f"{self.username}"
