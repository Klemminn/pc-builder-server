from django.contrib import admin
from .models import Build, Component

class BuildAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

admin.site.register(Build, BuildAdmin)

class ComponentAdmin(admin.ModelAdmin):
    list_display = ('id', 'build', 'content_type', 'content_object', 'created',)
    search_fields = ('build',)
    readonly_fields = ('created',)

admin.site.register(Component, ComponentAdmin)