from django.db import models
from django.forms import model_to_dict
from datetime import datetime
from config.settings import MEDIA_URL, STATIC_URL
# Create your models here.



#############################################################################33
#tomar de referencia

class servicio(models.Model):
    id_servicio= models.CharField("Id_servicio", max_length=20, primary_key=True)
    nombre = models.CharField("Nombre", max_length=20, null=True)
    costo= models.CharField("Costo", max_length=10, null=True)
    
    def __str__(self):
        return self.nombre
    
    def toJSON(self):
        item = model_to_dict(self)
        return item
    
##################################################################################



class Persona(models.Model):
    id=models.CharField(verbose_name='Rut',max_length=20 , unique=True, blank=False, null=False, primary_key=True)
    nombre=models.CharField(verbose_name='Nombre', max_length=50,  blank=False, null=False)
    apellido=models.CharField(verbose_name='Apellido',max_length= 50 , blank=False, null=False)
    direccion=models.CharField(verbose_name='Direccion',max_length= 120, blank=True, null=True)
    correo=models.EmailField(verbose_name='Correo', blank=False, null=False)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural='Personas'
        db_table= 'Persona'
        ordering=['id']

class Cliente(Persona):
    tipo= models.CharField('Tipo', max_length=50, null=True)


    def __str__(self):
        return self.id


    def toJSON(self):
        item = model_to_dict(self)
    
        return item
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural='Clientes'
        db_table= 'Cliente'
        ordering=['id'] 

class Empleado(Persona): 

    cargo=models.CharField(verbose_name='Cargo',max_length=25)
  
    def __str__(self):
        return self.id
    
    
    def toJSON(self):
        item = model_to_dict(self)
        # Agrega aquí cualquier otro campo que desees incluir en la JSON del empleado.
        return item

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural='Empleados'
        db_table= 'Empleado'
        ordering=['id']



class factura(models.Model):
    id= models.CharField("Total", max_length=10, primary_key=True)
    fecha_emision= models.CharField( "Fecha_emision", max_length=15, null=True)
    fecha_vencimiento = models.CharField("Fecha_vencimiento", max_length=15)
    def __str__(self):
        return self.id
    
    def toJSON(self):
        item = model_to_dict(self)
        return item

class detalles_facturas(models.Model):
    factura= models.ForeignKey(factura, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
    
    def toJSON(self):
        item = model_to_dict(self)
        item['factura.id'] = self.factura.toJSON()
        item['cliente.nombre'] = self.cliente.toJSON()
        return item

class ingresos(models.Model):
    factura = models.ForeignKey(factura, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
    
    def toJSON(self):
        item = model_to_dict(self)
        item['factura'] = self.factura.toJSON()
        return item


class detalles_servicio(models.Model):
    factura = models.ForeignKey(factura, on_delete=models.CASCADE)
    servicio = models.ForeignKey(servicio, on_delete=models.CASCADE)
    subtotal= models.CharField("Subtotal", max_length=15)

    def __str__(self):
        return str(self.id)
    
    def toJSON(self):
        item = model_to_dict(self)
        item['factura'] = self.factura.toJSON()
        item['servicio'] = self.servicio.toJSON()

        return item

class productos(models.Model):
    id= models.CharField("Id_Productos", max_length=10, primary_key=True)
    nombre= models.CharField("Nombre", max_length=20, null=True)
    precio_unitario= models.CharField("Precio_unitario", max_length=20, null=True)
    cantidad= models.CharField("Cantidad", max_length=20, null=True)
    cantidad_minima= models.CharField("Cantidad_minima", max_length=20, null=True)

    def __str__(self):
        return self.id
    
    def toJSON(self):
        item = model_to_dict(self)

        return item

class servicio_producto(models.Model):
    servicio = models.ForeignKey(servicio, on_delete=models.CASCADE)
    productos = models.ForeignKey(productos, on_delete=models.CASCADE)
    cantidad = models.CharField("Cantidad",max_length=20)
    costo = models.CharField("Costo", max_length=15)

class salidas_fijas(models.Model):
    id= models.CharField("Nombre", max_length=20, primary_key=True)
    fecha = models.CharField("Fecha", max_length=20)
    monto = models.CharField("Monto", max_length=15)

    def __str__(self):
        return str(self.id)
    
    def toJSON(self):
        item = model_to_dict(self)

        return item

class proveedores(models.Model):
    id= models.CharField("Fecha_Pago", max_length=15, primary_key=True)
    monto= models.CharField("Monto", max_length=15)

    def __str__(self):
        return str(self.id)
    
    def toJSON(self):
        item = model_to_dict(self)

        return item

class Egresos(models.Model):
    proveedores = models.ForeignKey(proveedores, on_delete=models.CASCADE)
    salidas_fijas = models.ForeignKey(salidas_fijas, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
    
    def toJSON(self):
        item = model_to_dict(self)
        item['proveedores'] = self.proveedores.toJSON()
        item['salidas_fijas'] = self.salidas_fijas.toJSON()

        return item

