from django.contrib import admin
from .models import Events
# Register your models here.
class EventsAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'starting_date',)

admin.site.register(Events, EventsAdmin)