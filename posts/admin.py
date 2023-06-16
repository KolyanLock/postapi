from django import forms
from django.contrib import admin
from django.utils.html import format_html

from .models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    save_on_top = True
    list_display = ('id', 'title', 'slug', 'author', 'category', 'created_at', 'is_published', 'display_image')
    list_display_links = ('id', 'title')
    list_filter = ('category', 'is_published')
    list_editable = ('is_published',)
    fields = (
        'id', 'title', 'slug', 'image', 'content', 'author', 'category', 'tags', 'updated_at', 'created_at',
        'views',
        'is_published')
    readonly_fields = ('id', 'author', 'created_at', 'updated_at', 'views')

    def display_image(self, obj):
        if obj.image:
            return format_html(f'<a href="{obj.image.url}" target="_self"><img src="{obj.image.url}" width="75" /></a>')
        return None

    display_image.short_description = 'Картинка'

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
