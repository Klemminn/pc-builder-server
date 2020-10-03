from django.utils.html import format_html
from django.contrib import admin
from .models import Retailer, Offering

@admin.register(Retailer)
class RetailerAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'website', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

@admin.register(Offering)
class OfferingAdmin(admin.ModelAdmin):
    list_display = ('id', 'retailer', 'name', 'price', 'content_type', 'content_object', 'show_url', 'disabled', 'created',)
    list_display_links = ('id', 'content_object')
    search_fields = ('build',)
    readonly_fields = ('created',)

    def show_url(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.url)

    show_url.short_description = "Url"
