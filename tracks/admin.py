from django.contrib import admin

from tracks.models import Track

# Register your models here.


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "posted_by")
