from django.contrib import admin
from .models import Info,Seat


class InfoAdmin(admin.ModelAdmin):
    list_display=['name','uid','seatnumber']
    exclude = ('seatnumber',)
class SeatAdmin(admin.ModelAdmin):
    list_display=['seatnumber','isavailable']
admin.site.register(Info,InfoAdmin)
admin.site.register(Seat,SeatAdmin)