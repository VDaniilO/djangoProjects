from django.contrib import admin

from .models import logInf, Regions

# Register your models here.

class logInfAdmin(admin.ModelAdmin):
    list_display = ( 'email', 'firstName', 'lastName', 'created_at', 'update_up', 'region', 'active')
    list_display_links = ( 'email', 'firstName', 'lastName')
    search_fields = ('email', 'region', 'firstName', 'lastName')
    list_editable = ('active',)
    lsit_filter = ('region', 'active')

class RegionsAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'Region_name')
    list_display_links = ( 'Region_name',)
    search_fields = ('Region_name',)

admin.site.register(logInf, logInfAdmin)
admin.site.register(Regions, RegionsAdmin)
