from django.contrib import admin

from core import core_models

@admin.register(core_models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'login', 'email', 'pro_user')

@admin.register(core_models.Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_name', 'verification', 'first_name', 'last_name', 'city', 'country')

@admin.register(core_models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'follower_counter', 'following_counter', 'track_counter', 'like_counter')   

@admin.register(core_models.SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')     

@admin.register(core_models.Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'artist', 'public_access', 'publish_date', 'play_counter', 'like_counter', 'repost_counter', 'comment_counter')

@admin.register(core_models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'artist', 'comment')

@admin.register(core_models.Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'artist', 'track', 'like')    

@admin.register(core_models.Repost)
class RepostAdmin(admin.ModelAdmin):
    list_display = ('id', 'artist', 'track', 'repost')

