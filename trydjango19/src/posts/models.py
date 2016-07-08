from __future__ import unicode_literals

from django.conf import settings 
from django.core.urlresolvers import reverse
from django.db import models

from django.utils.encoding import smart_unicode
#from django.db.models.signals import pre_save

#from django.utils.text import slugify

# Create your models here.
#MVC
#def upload_location(instance, filename):
#	return "%s/%s"%(instance.id,filename)


class PostManager(models.Manager):
	def active(self, *args, **kwargs):
		return super(PostManager,self).filter(draft=False).filter(publish__lte=timezone.now())



class Post(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
	title = models.CharField(max_length=120)
	image = models.FileField(null=True, blank=True)
	#image = models.ImageField(upload_to=upload_location,
	#	null=True, 
	#	blank=True,
	#	width_field="width_field",
	#	height_field="height_field")
	#height_field = models.IntegerField(default=0)
	#width_field = models.IntegerField(default=0)
	content = models.TextField()
	draft = models.BooleanField(default=False)
	publish = models.DateField(auto_now=False,auto_now_add=False)
	updated = models.DateTimeField(auto_now=True,auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)


# class SignUp(models.Model):
# 	first_name = models.CharField(max_length=120, null=True,blank=True)
# 	last_name = models.CharField(max_length=120, null=True,blank=True)
# 	email = models.EmailField()
# 	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
# 	updated = models.DateTimeField(auto_now_add=False, auto_now=True)





# 	objects = PostManager()
# 	def __unicode__(self):
# 		return smart_unicode(self.email)

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title	

	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"id": self.id})
	
	class Meta:
		ordering = ["-timestamp", "-updated"]


#def pre_save_post_receiver(sender, instance, *args, **kwargs):
#	slug = slugify(instance.title)
#	eixsts = Post.objects.filter(slug=slug).eixsts()
#	if eixsts:
#		slug = "%s-%s" %(slug, instance.id)

#	instance.slug = slug	


#pre_save.connect(pre_save_post_receiver,sender=Post)			