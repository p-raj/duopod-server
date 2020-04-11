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


@admin.register(models.ListenStats)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'episode', 'listened_by', 'language')
    list_display_links = ('id',)
    search_fields = ('episode.title',)
    list_per_page = 20
    ordering = ('-id',)


@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'label')
    list_display_links = ('label',)
    search_fields = ('name', )
    list_per_page = 20


@admin.register(models.EpisodeLanguageMapping)
class EpisodeLanguageMappingAdmin(admin.ModelAdmin):
    list_display = ('id', 'language', 'episode', 'link')
    list_display_links = ('language',)
    show_full_result_count = False
