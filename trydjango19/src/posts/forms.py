from django import forms
from .models import Post


import re
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = [
			"title",
			"content",
			"image",
			"draft",
			"publish",
		]

 