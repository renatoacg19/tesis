from django.contrib import admin
from core.home.models import *
# Register your models here.

admin.site.register(servicio)
admin.site.register(Empleado)
admin.site.register(detalles_servicio)
admin.site.register(detalles_facturas)
admin.site.register(factura)
admin.site.register(proveedores)
admin.site.register(productos)
admin.site.register(servicio_producto)
admin.site.register(ingresos)
admin.site.register(Egresos)
admin.site.register(salidas_fijas)
admin.site.register(Cliente)