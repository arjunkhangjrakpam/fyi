from django.shortcuts import render
from django.http import HttpResponse
#from .models import Post
#from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#from django.contrib.auth.mixins import UserPassesTestMixin
#from django.views.generic.dates import YearArchiveView
	

def index(request):
    return render(request, 'blog/index.html')


posts = [

{
  'author' : 'Loonycorn',
  'title' : 'Blog Post 1',
  'content' : 'First post content',
  'date_posted' : 'October 25, 2019'
},
{
  'author' : 'Test',
  'title' : 'Blog Post 2',
  'content' : 'Second post content',
  'date_posted' : 'October 26, 2019'
}

]	



def nda_na(request):
	context = {

  'posts' : posts

   }
	return render(request, 'blog/nda_na.html',context)

def rimc(request):
	context = {

  'posts' : posts

   }
	return render(request, 'blog/rimc.html',context)

def ssb(request):
	context = {

  'posts' : posts

   }
	return render(request, 'blog/ssb.html',context)


