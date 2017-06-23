from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from .models import Producto, Ciudad, Proveedor, Cliente
from .forms import ProductoForm, CiudadForm, ProveedorForm, ClienteForm


# Create your views here.

class ProductosCreate(CreateView):
	model = Producto
	template_name = "ingreso_producto.html"
	form_class = ProductoForm 
	success_url = reverse_lazy('inventarios:producto')

	def get_context_data(self, **kwargs):
		context = super(ProductosCreate, self).get_context_data(**kwargs)
		if 'form' not in context: 
			context['form'] = self.form_class(self.request.GET)
		context['producto_list'] = Producto.objects.all()
		return context 

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form))

def productoUpdate(request, id_producto):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	producto = Producto.objects.get(id=id_producto)
	if request.method == 'GET':
		form = ProductoForm(instance=producto)
	else:
		form = ProductoForm(request.POST, instance=producto)
		if form.is_valid():
			form.save()
		return redirect("inventarios:producto")
	return render(request, "ingreso_producto.html", {'form':form})

class ProductoDelete(DeleteView):
	model = Producto
	template_name = "producto_delete.html"
	form_class = ProductoForm
	success_url = reverse_lazy("inventarios:producto")

class ProductoList(ListView):
	model = Producto
	template_name = "lista_producto.html"

def ingresarCiudad(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	form = CiudadForm(request.POST or None)
	queryset_list = Ciudad.objects.all()
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		messages.success(request, "Ciudad Agregada")
		return redirect("inventarios:listado")
	context = {
		"form":form,
		"lista_ciudad": queryset_list,
		"title": "Agregar Ciudad"
	}
	return render(request, "ingreso_ciudad.html", context)

def ingresarProveedor(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	form = ProveedorForm(request.POST or None)
	queryset_list = Proveedor.objects.all()
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		messages.success(request, "Proveedor Agregado")
		return redirect("inventarios:proveedor")
	context = {
		"form":form, 
		"lista_proveedor":queryset_list,
		"title": "Agregar Proveedor"
	}
	return render(request, "ingreso_proveedor.html", context)


# Vista basada en clases. 
class CiudadList(ListView):
	model = Ciudad
	template_name = "listado.html"

class CiudadUpdate(UpdateView):
	model = Ciudad
	template_name = "ingreso_ciudad.html"
	form_class = CiudadForm 
	success_url = reverse_lazy('inventarios:ciudad')

	def get_context_data(self, **kwargs):
		context = super(CiudadUpdate, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk', 0)
		codCiudad = self.model.objects.get(id=pk)
		queryset_list = self.model.objects.all()
		if 'form' not in context: 
			context['form'] = self.form_class()
		context['id'] = pk
		return context 

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		id_ciudad = kwargs['pk']
		codCiudad = self.model.objects.get(id=id_ciudad)
		form = self.form_class(request.POST, instance=codCiudad)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return HttpResponseRedirect(self.get_success_url())

	def form_valid(self, form):
		form.instance = self.request.user
		return super(CiudadUpdate, self).form_valid(form)


class CiudadDelete(DeleteView):
	model = Ciudad
	template_name = "ciudad_delete.html"
	success_url = reverse_lazy('inventarios:ciudad')

class ProveedorUpdate(UpdateView):
	model = Proveedor
	template_name = "ingreso_proveedor.html"
	form_class = ProveedorForm
	success_url = reverse_lazy('inventarios:proveedor')

	def get_context_data(self, **kwargs):
		context = super(ProveedorUpdate, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk', 0)
		codProveedor = self.model.objects.get(id=pk)
		if 'form' not in context: 
			context['form'] = self.form_class()
		context['id'] = pk
		return context
	def post(self, request, *args, **kwargs):
		self.object = self.get_object 
		id_proveedor = kwargs['pk']
		codProveedor = self.model.objects.get(id=id_proveedor)
		form = self.form_class(request.POST, instance=codProveedor)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return HttpResponseRedirect(self.get_success_url())

class ProveedorDelete(DeleteView):
	model = Proveedor
	template_name = "proveedor_delete.html"
	form_class = ProveedorForm
	success_url = reverse_lazy('inventarios:proveedor')

class ClienteCreate(CreateView):
	model = Cliente
	template_name = "ingreso_cliente.html"
	form_class = ClienteForm
	success_url = reverse_lazy('inventarios:cliente')

	def get_context_data(self, **kwargs):
			context = super(ClienteCreate, self).get_context_data(**kwargs)
			if 'form' not in context: 
				context['form'] = self.form_class(self.request.GET)
			context['cliente_list'] = Cliente.objects.all()
			return context 

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form))