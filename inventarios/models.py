from django.db import models

# Create your models here.

def upload_location(instance, filename):
	return "%s/%s" %(instance.id, filename)

class Ciudad(models.Model):
	nombreCiudad = models.CharField(max_length=50, null=True, blank=True)

	def __str__(self):
		return '{}'.format(self.nombreCiudad)
	
class Proveedor(models.Model):
	nombreProveedor = models.CharField(max_length=50, null=True, blank=True)
	direccionProveedor = models.CharField(max_length=50, null=True, blank=True)
	telefonoProveedor = models.IntegerField(null=True, blank=True)
	ciudad = models.ForeignKey(Ciudad, null=True, blank=True, on_delete=models.CASCADE)

	def __unicode__(self):
		return self.title

	def __str__(self):
		return '{}'.format(self.nombreProveedor)

class Producto(models.Model):
	nombreProducto = models.CharField(max_length=50, null=True, blank=True)
	stockProducto = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
	precioCostoProducto = models.IntegerField(null=True, blank=True)
	precioVentaProducto = models.IntegerField(null=True, blank=True)
	proveedor = models.ForeignKey(Proveedor, null=True, blank=True, on_delete=models.CASCADE)

	def __unicode__(self):
		return self.title

	def __str__(self):
		return '{}'.format(self.nombreProducto)

class Cliente(models.Model):
	nombreCliente = models.CharField(max_length=50, null=True, blank=True)
	ciudadCliente = models.ForeignKey(Ciudad, null=True, blank=True, on_delete=models.CASCADE)
	direccionCliente = models.CharField(max_length=50, null=True, blank=True)

class Factura(models.Model):
	numeroFactura = models.IntegerField(null=True, blank=True)
	fechaFactura = models.DateTimeField(auto_now=False)
	totalFactura = models.IntegerField(null=True, blank=True)
	ivaFactura = models.IntegerField(null=True, blank=True)
	proveedor = models.ForeignKey(Proveedor, null=True, blank=True, on_delete=models.CASCADE)

class DetalleFactura(models.Model):
	producto = models.ManyToManyField(Producto)
	factura = models.ForeignKey(Factura, null=True, blank=True, on_delete=models.CASCADE)
	cantidadDetalle = models.IntegerField(null=True, blank=True)
	totalDetalle = models.IntegerField(null=True, blank=True)


