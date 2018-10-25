from django.contrib import admin
from .models import Team,CompanyAbouts
# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    list_display = ( 'first_name', 'last_name')

class CompanyAboutsAdmin(admin.ModelAdmin):
    list_display = ( 'heading', 'description')
admin.site.register(Team, TeamAdmin)
admin.site.register(CompanyAbouts, CompanyAboutsAdmin)