from django.urls import path

from core.home.views.inicio.views import *

from core.home.views.servicios.views import *

from core.home.views.empleado.views import *

from core.home.views.facturas.views import *

from core.home.views.detalles.views import *

from core.home.views.ingresos.views import *

from core.home.views.productos.views import *

from core.home.views.proveedores.views import *

from core.home.views.egresos.views import *

from core.home.views.salidas_fijas.views import *

from core.home.views.detalles_servicio.views import *

from core.home.views.clientes.views import *

app_name = 'home'

urlpatterns = [
        #home
    path('inicio/', InicioView.as_view(), name='inicio'),
    
    #servicios
    path('sv/list', ServicioListView.as_view(), name='servicio_list'),
    path('sv/add/', ServicioCreateView.as_view(), name='servicio_create'),
    path('sv/update/<str:pk>/', ServicioUpdateView.as_view(), name='servicio_update'),
    path('sv/delete/<str:pk>/', ServicioDeleteView.as_view(), name='servicio_delete'),

    #empleados
    path('empleado/list', EmpleadoListView.as_view(), name='empleado_list'),
    path('empleado/add/', EmpleadoCreateView.as_view(), name='empleado_create'),
    path('empleado/update/<str:pk>/', EmpleadoUpdateView.as_view(), name='empleado_update'),
    path('empleado/delete/<str:pk>/', EmpleadoDeleteView.as_view(), name='empleado_delete'),

    #facturas
    path('facturas/list', FacturaListView.as_view(), name='factura_list'),
    path('facturas/add/', FacturasCreateView.as_view(), name='factura_create'),
    path('facturas/update/<str:pk>/', FacturaUpdateView.as_view(), name='factura_update'),
    path('facturas/delete/<str:pk>/', FacturaDeleteView.as_view(), name='factura_delete'),

#detalles_facturas
    path('detalles_facturas/list', Detalles_facturasListView.as_view(), name='detalles_facturas_list'),
    path('detalles_facturas/add/', Detalles_facturasCreateView.as_view(), name='detalles_facturas_create'),
    path('detalles_facturas/update/<str:pk>/',Detalles_facturasUpdateView.as_view(), name='detalles_facturas_update'),
    path('detalles_facturas/delete/<str:pk>/',Detalles_facturasDeleteView.as_view(), name='detalles_facturas_delete'),

    path('ingresos/list', IngresosListView.as_view(), name='ingresos_list'),
    path('ingresos/add/', IngresosCreateView.as_view(), name='ingresos_create'),
    path('ingresos/update/<str:pk>/',IngresosUpdateView.as_view(), name='ingresos_update'),
    path('ingresos/delete/<str:pk>/',IngresosDeleteView.as_view(), name='ingresos_delete'),

    path('productos/list', ProductosListView.as_view(), name='productos_list'),
    path('productos/add/', ProductosCreateView.as_view(), name='productos_create'),
    path('productos/update/<str:pk>/', ProductosUpdateView.as_view(), name='productos_update'),
    path('productos/delete/<str:pk>/', ProductosDeleteView.as_view(), name='productos_delete'),

    path('proveedores/list', ProveedoresListView.as_view(), name='proveedores_list'),
    path('proveedores/add/', ProveedoresCreateView.as_view(), name='proveedores_create'),
    path('proveedores/update/<str:pk>/', ProveedoresUpdateView.as_view(), name='proveedores_update'),
    path('proveedores/delete/<str:pk>/', ProveedoresDeleteView.as_view(), name='proveedores_delete'),

    path('egresos/list', EgresosListView.as_view(), name='egresos_list'),
    path('egresos/add/', EgresosCreateView.as_view(), name='egresos_create'),
    path('egresos/update/<str:pk>/', EgresosUpdateView.as_view(), name='egresos_update'),
    path('egresos/delete/<str:pk>/', EgresosDeleteView.as_view(), name='egresos_delete'),

    path('salidas_fijas/list', Salidas_fijasListView.as_view(), name='salidas_fijas_list'),
    path('salidas_fijas/add/', Salidas_fijasCreateView.as_view(), name='salidas_fijas_create'),
    path('salidas_fijas/update/<str:pk>/', Salidas_fijasUpdateView.as_view(), name='salidas_fijas_update'),
    path('salidas_fijas/delete/<str:pk>/', Salidas_fijasDeleteView.as_view(), name='salidas_fijas_delete'),

    path('detalles_servicio/list', Detalles_servicioListView.as_view(), name='detalles_servicio_list'),
    path('detalles_servicio/add/', Detalles_servicioCreateView.as_view(), name='detalles_servicio_create'),
    path('detalles_servicio/update/<str:pk>/', Detalles_servicioUpdateView.as_view(), name='detalles_servicio_update'),
    path('detalles_servicio/delete/<str:pk>/', Detalles_servicioDeleteView.as_view(), name='detalles_servicio_delete'),

    path('cliente/list', ClienteListView.as_view(), name='cliente_list'),
    path('cliente/add/', ClienteCreateView.as_view(), name='cliente_create'),
    path('cliente/update/<str:pk>/', ClienteUpdateView.as_view(), name='cliente_update'),
    path('cliente/delete/<str:pk>/', ClienteDeleteView.as_view(), name='cliente_delete'),
]