from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.db.models import Q
from .models import Retailer, Offering, Scrape

@admin.register(Retailer)
class RetailerAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'website', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

class OfferingIgnoredFilter(admin.SimpleListFilter):

    title = _('Ignored')

    parameter_name = 'ignored'

    def lookups(self, request, model_admin):
        return (
            ('ignored_or_disabled', _('Ignored or Disabled')),
        )
    
    """Choices supplied to remove the "All" Option"""
    def choices(self, changelist):
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == _(lookup),
                'query_string': changelist.get_query_string({self.parameter_name: lookup}, []),
                'display': title,
            }

    def queryset(self, request, queryset):
        if self.value() == 'ignored_or_disabled':
            return queryset.filter(Q(ignored=True) | Q(disabled=True))
        return queryset.filter(ignored=False).filter(disabled=False)


@admin.register(Offering)
class OfferingAdmin(admin.ModelAdmin):
    list_display = ('id', 'retailer', 'name', 'price', 'content_type', 'object_id', 'content_object', 'show_url', 'disabled', 'ignored', 'created',)
    list_display_links = ('id', 'name',)
    list_editable = ('object_id', 'ignored', )
    search_fields = ('name',)
    readonly_fields = ('created',)
    list_filter = (('content_type', admin.RelatedOnlyFieldListFilter,),OfferingIgnoredFilter,)
    list_per_page = 300
    default_filter = ('ignored__exact=False',)

    def show_url(self, obj):
        return format_html("<a href='{url}' target='_blank'>{url}</a>", url=obj.url)

    show_url.short_description = "Url"

@admin.register(Scrape)
class ScrapeAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_offerings', 'new_offerings', 'created',)
    readonly_fields = ('created',)
