from django.contrib import admin

from tracks.models import (
    Track,
    Like,
)

# Register your models here.


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "posted_by")


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "track", "created_at")
