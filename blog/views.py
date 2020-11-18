from django.shortcuts import render
from django.http import HttpResponse
#from .models import Post
#from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#from django.contrib.auth.mixins import UserPassesTestMixin
#from django.views.generic.dates import YearArchiveView
	

def index(request):
    return HttpResponse("WELCOME TO DJANGO BLOG")
	#return render(request, 'blog/index.html')

def setup(request):
	context = {

	'posts' : Post.objects.all()

	}
	return render(request, 'blog/setup.html',context)
