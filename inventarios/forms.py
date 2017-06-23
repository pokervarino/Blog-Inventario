from django import forms
from .models import Producto, Ciudad, Proveedor, Cliente

class CiudadForm(forms.ModelForm):
	class Meta: 
		model = Ciudad 
		fields = [
		   'nombreCiudad',
		]
		labels = {
		   'nombreCiudad': 'Nombre de Ciudad'
		}
class ProveedorForm(forms.ModelForm):
	class Meta: 
		model = Proveedor
		fields = [
		   'nombreProveedor',
		   'direccionProveedor',
		   'telefonoProveedor',
		   'ciudad',
		]

		labels = {
			'nombreProveedor': 'Proveedor',
			'direccionProveedor': 'Direccion',
			'telefonoProveedor': 'Telefono',
			'ciudad': 'Ciudad',
		}
		widgets = {
			'ciudad': forms.Select(),
		}

class ProductoForm(forms.ModelForm):
	class Meta:
		model = Producto
		fields = [
			'nombreProducto',
			'stockProducto',
			'precioCostoProducto',
			'precioVentaProducto',
			'proveedor',
		]
		labels = {
			'nombreProducto': 'Nombre del Producto',
			'stockProduto': 'Stock',
			'precioCostoProducto': 'Precio Costo',
			'precioVentaProducto': 'Precio Venta',
			'proveedor': 'Proveedor',
		}
		widgets = {
			'nombreProducto': forms.TextInput(attrs={'class':'form-control'}),
			'stockProducto': forms.TextInput(attrs={'class':'form-control'}),
			'precioCostoProducto':forms.TextInput(attrs={'class':'form-control'}),
			'precioVentaProducto':forms.TextInput(attrs={'class':'form-control'}),
			'proveedor': forms.Select(attrs={'class':'form-control'}),
		}

class ClienteForm(forms.ModelForm):
	class Meta: 
		model = Cliente
		fields = [
            'nombreCliente',
            'ciudadCliente',
            'direccionCliente',
		]
		labels = {
		    'nombreCliente': 'Nombre del Cliente',
		    'ciudadCliente': 'Ciudad',
		    'direccionCliente': 'Direccion',
		}
		widgets = {
			'nombreCliente': forms.TextInput(attrs={'class':'form-control'}),
			'ciudadCliente': forms.Select(attrs={'class':'form-control'}),
			'direccionCliente': forms.TextInput(attrs={'class':'form-control'}),
		}