from __future__ import unicode_literals
from django.db import models
from django.conf import settings

from django.core.urlresolvers import reverse 
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.utils import timezone 
from django.utils.safestring import mark_safe

from markdown_deux import markdown


# Create your models here.

# class PostManager(models.Manager):
# 	def active(self, *args, **kwargs):
# 		return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())

def upload_location(instance, filename):
	return "%s/%s" %(instance.id, filename)

class Post(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	title = models.CharField(max_length=120)
	slug = models.SlugField(unique=True)
	image = models.ImageField(upload_to=upload_location, null=True, blank=True,
			width_field="width_field",
			height_field="height_field")
	width_field= models.IntegerField(default=0)
	height_field= models.IntegerField(default=0)
	content = models.TextField()
	publish = models.DateField(auto_now=False, auto_now_add=False)
	timestamp = models.DateField(auto_now=False, auto_now_add=True)


	def __unicode__(self):
		return self.title
		
	def __str__(self):
		return self.title

	def get_markdown(self):
		content = self.content
		markdown_text = markdown(content)
		return mark_safe(markdown_text)

	def get_absolute_url(self):
		return reverse("blog:detail", kwargs={"slug": self.slug})

def create_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = Post.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists: 
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)
# 	if instance.content:
# 		html_string = instance.get_markdown()
# 		read_time_var = get_read_time(html_string)
# 		instance.read_time = read_time_var	

pre_save.connect(pre_save_post_receiver, sender=Post)