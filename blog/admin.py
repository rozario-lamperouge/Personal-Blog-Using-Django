from django.contrib import admin
from django.db import models
from .models import Post
from tinymce.widgets import TinyMCE

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	fieldsets = [
		('Title/Date', {"fields" : ['title','date']}),
		('Content',{'fields':['body']})
	]
	formfield_overrides = {
    	models.TextField: {'widget': TinyMCE()}
    }
    
admin.site.register(Post, PostAdmin)

