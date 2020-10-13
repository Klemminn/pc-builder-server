from django.contrib import admin
from .models import Build

@admin.register(Build)
class BuildAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'offerings', 'created',)
    search_fields = ('offerings',)
    readonly_fields = ('created',)
