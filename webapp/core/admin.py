from django.contrib import admin

from core import models

@admin.register(models.Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_name', 'verification', 'first_name', 'last_name', 'city', 'country')

@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'follower_counter', 'following_counter', 'track_counter', 'like_counter')   

@admin.register(models.SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')     

@admin.register(models.Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'public_access', 'publish_date', 'play_counter', 'like_counter', 'repost_counter', 'comment_counter')

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'date')

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'like')    

@admin.register(models.Repost)
class RepostAdmin(admin.ModelAdmin):
    list_display = ('id', 'repost')

