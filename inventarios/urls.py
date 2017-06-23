from django.conf.urls import url
from django.contrib import admin 

from .views import (
	ingresarCiudad,
	ingresarProveedor,
	CiudadList,
	CiudadUpdate,
	CiudadDelete,
	ProveedorUpdate,
	ProveedorDelete,
	ProductosCreate,
	productoUpdate,
	ProductoDelete,
	ProductoList,
	ClienteCreate
 	#ingresarProducto
	#detalleProducto,
	#listaProducto
	#eliminarProducto,
	#editarProducto,
	)

urlpatterns = [
	url(r'^producto/$', ProductosCreate.as_view(), name='producto'),
	url(r'^listado$', CiudadList.as_view(), name='listado'),
	url(r'^ciudad/$', ingresarCiudad, name='ciudad'),
	url(r'^proveedor/$', ingresarProveedor, name='proveedor'),
	url(r'^ciudad/editar/(?P<pk>\d+)$', CiudadUpdate.as_view(), name='editar'),
	url(r'^ciudad/eliminar/(?P<pk>\d+)$', CiudadDelete.as_view(), name='eliminar'),
	url(r'^proveedor/editar/(?P<pk>\d+)$', ProveedorUpdate.as_view(), name='proveedor_editar'),
	url(r'^proveedor/eliminar/(?P<pk>\d+)$', ProveedorDelete.as_view(), name='proveedor_eliminar'),
	url(r'^producto/editar/(?P<id_producto>\d+)$', productoUpdate, name='producto_editar'),
	url(r'^producto/eliminar/(?P<pk>\d+)$', ProductoDelete.as_view(), name='producto_eliminar'),
	url(r'^lista$', ProductoList.as_view(), name='lista'),
	url(r'^cliente/$', ClienteCreate.as_view(), name='cliente'),
]

