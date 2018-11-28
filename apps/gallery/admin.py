from django.contrib import admin
from .models import Album, Image


class ImageInline(admin.TabularInline):
    model = Image


class AlbumAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_filter = ('is_featured',)

admin.site.register(Album, AlbumAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_filter = ('album','is_featured')


admin.site.register(Image, ImageAdmin)
