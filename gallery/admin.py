from django.contrib import admin
from .models import Gallery
# Register your models here.
class GalleryAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'created_date',)

admin.site.register(Gallery, GalleryAdmin)