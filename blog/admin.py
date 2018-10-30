from django.contrib import admin
from .models import Blogs,BlogComments,BlogBanner
# Register your models here.
class BlogsAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'posting_date',)


class BlogCommentsAdmin(admin.ModelAdmin):
    list_display = ( 'first_name', 'posting_date',)

class BlogBannerAdmin(admin.ModelAdmin):
    list_display = ( 'heading', 'created_date', 'content')

admin.site.register(BlogBanner, BlogBannerAdmin)

admin.site.register(Blogs, BlogsAdmin)
admin.site.register(BlogComments, BlogCommentsAdmin)