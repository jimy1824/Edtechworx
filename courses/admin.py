from django.contrib import admin
from .models import Course
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'description', 'trainer_name')

admin.site.register(Course, CourseAdmin)