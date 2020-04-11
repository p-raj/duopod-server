from django.contrib import admin

# Register your models here.
from podcasts import models


@admin.register(models.Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_per_page = 20
    ordering = ('-id',)


@admin.register(models.Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    list_display_links = ('id',)
    search_fields = ('title',)
    list_per_page = 20
    ordering = ('-id',)
