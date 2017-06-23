from django import forms

from pagedown.widgets import PagedownWidget 
from .models import Post 

class PostForm(forms.ModelForm):
	content = forms.CharField(label='Contenido',widget=PagedownWidget(show_preview=False))
	publish = forms.DateField(label='Fecha Publicacion', widget=forms.SelectDateWidget)

	class Meta:
		model = Post
		fields = [
           "title",
           "image",
           "content",
           "publish",
		]	
		labels = {
			"title": "Titulo",
			"image": "Imagen",
		}