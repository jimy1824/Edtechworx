from django.contrib import admin
from .models import HomeBanner
# Register your models here.
class HomeBannerAdmin(admin.ModelAdmin):
    list_display = ( 'heading', 'created_date', 'content')

admin.site.register(HomeBanner, HomeBannerAdmin)