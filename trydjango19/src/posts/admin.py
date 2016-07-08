from django.contrib import admin

# Register your models here.
from .models import Post
# from .models import Post, SignUp

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title","updated","timestamp"]
	list_display_link = ["updated"]
	list_editable = ["title"]
	list_filter = ["updated", "timestamp"]
	
	search_fields = ["title", "content"]
	class Meta:
		model = Post

# class SignUpAdmin(admin.ModelAdmin):
# 	class Meta:
# 		model = SignUp
	


admin.site.register(Post,PostModelAdmin)

# admin.site.register(SignUp, SignUpAdmin)