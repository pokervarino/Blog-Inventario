from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType 
from django.db.models import Q 
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect


from .models import Post 
from .forms import PostForm

# Create your views here.

def blog_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404

	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user 
		instance.save()
		messages.success(request, "Tema creado exitosamente")
		return HttpResponseRedirect(instance.get_absolute_url())
		
	context = {
		"form": form,
	}

	return render(request, "blog_form.html", context)

def blog_list(request):
	queryset_list = Post.objects.all().order_by("-timestamp")
	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
			Q(title__icontains=query)|
			Q(content__icontains=query)|
			Q(user__username__icontains=query)
			).distinct()
	paginator = Paginator(queryset_list, 5)
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger: 
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)
	context = {
		"object_list": queryset_list,
		"title": "Recetas"

	}

	return render(request, "blog_list.html", context)


def blog_detail(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	#share_tring = quote_plus(instance.content)

	context = {
		"title": instance.title,
		"instance": instance,
		#"share_string": share_string
	}

	return render(request, "blog_detail.html", context)

def blog_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	messages.success(request, "Post Eliminado Correctamente")
	return redirect("blog:list")

def blog_update(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Post Editado")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"title": instance.title,
		"instance": instance,
		"form": form 
	}
	return render (request, "blog_form.html", context)