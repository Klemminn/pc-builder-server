from django.utils.html import format_html
from django.contrib import admin
from .models import Build

@admin.register(Build)
class BuildAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'show_url', 'offerings', 'created',)
    search_fields = ('offerings',)
    readonly_fields = ('created',)

    def show_url(self, obj):
        return format_html("<a href='https://builder.vaktin.is/build/{code}' target='__blank'>Builder link</a>", code=obj.code)

    show_url.short_description = "Url"
