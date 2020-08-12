from django.contrib import admin

# Register your models here.
from .models import Person, Content, Downloads


class DownloadsAdmin(admin.ModelAdmin):
    list_display = ('person', 'content', 'downloads')
    search_fields = ('person', 'content')


admin.site.register(Downloads, DownloadsAdmin)


class PersonAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'email', 'name')


admin.site.register(Person, PersonAdmin)


class ContentAdmin(admin.ModelAdmin):
    list_display = ('content_slug', 'drive_link', 'is_active')
    search_fields = ('content_slug',)


admin.site.register(Content, ContentAdmin)
