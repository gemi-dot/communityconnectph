
# Register your models here.
from django.contrib import admin
from .models import WaterStation, WaterRefillRequest



@admin.register(WaterStation)
class WaterStationAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_person', 'phone_number')

@admin.register(WaterRefillRequest)
class WaterRefillRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'container_type', 'quantity', 'status', 'assigned_station')
    list_filter = ('status', 'assigned_station')
    search_fields = ('name', 'phone_number')
