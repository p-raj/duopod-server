from django.contrib import admin

# Register your models here.
from users import models


@admin.register(models.UserType)
class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'type')
    list_display_links = ('id',)
    search_fields = ('name', )
    list_per_page = 20
    ordering = ('-id',)
