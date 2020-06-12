from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post


class PostList(ListView):
	queryset = Post.objects.order_by('-date')
	template_name = 'blog/blog.html'

def post(request, id):
	post = Post.objects.get(id=id)
	return render(request,'blog/post.html',{'post':post})