from django.contrib import admin

from users import models

@admin.register(models.UserSite)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'pro_user')