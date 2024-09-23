from django.contrib import admin

from .models import *


class IconsAdmin(admin.ModelAdmin):
    list_display = ('picture', 'title', 'description', 'weight', 'category')
    list_display_links = ('title',)
    list_editable = ('weight',)
    list_filter = ('category',)
    search_fields = ('title', 'description')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


admin.site.register(Icons)
admin.site.register(Category)
