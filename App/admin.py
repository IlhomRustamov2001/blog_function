from django.contrib import admin
from .models import *

@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
    fields=['name', 'content', 'slug', 'image', 'user']
    prepopulated_fields={'slug':('name',)}

@admin.register(Blog)
class Blogadmin(admin.ModelAdmin):
    fields=['title', 'slug', 'content', 'image', 'user', 'tags', 'views']
    prepopulated_fields={'slug':('title',)}

@admin.register(Tag)
class Tagadmin(admin.ModelAdmin):
    list_display=['name', 'slug']
    prepopulated_fields={'slug': ('name',)}

@admin.register(Comment)
class Commentadmin(admin.ModelAdmin):
    list_display=['blog', 'user', 'created_at', 'text']

