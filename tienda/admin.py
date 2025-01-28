from django.contrib import admin
from .models import Servicio, Venta
# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class VentaAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Venta, VentaAdmin)