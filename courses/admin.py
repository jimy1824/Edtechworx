from django.contrib import admin
from .models import Course ,CoursesBanner,CourseComments
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'description', 'trainer_name')


class CoursesBannerAdmin(admin.ModelAdmin):
    list_display = ( 'heading', 'created_date')

class CoursesCommentsAdmin(admin.ModelAdmin):
    list_display = ( 'first_name', 'posting_date',)

admin.site.register(CourseComments, CoursesCommentsAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(CoursesBanner, CoursesBannerAdmin)