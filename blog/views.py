from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .models import Post_rimc
from .models import Post_ssb

#from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#from django.contrib.auth.mixins import UserPassesTestMixin
#from django.views.generic.dates import YearArchiveView
	

def index(request):
    return render(request, 'blog/index.html')


def nda_na(request):
	context = {

  'posts' : Post.objects.all()

   }
	return render(request, 'blog/nda_na.html',context)

def rimc(request):
	context = {

  'posts' : Post_rimc.objects.all()


   }
	return render(request, 'blog/rimc.html',context)

def ssb(request):
	context = {

  'posts' : Post_ssb.objects.all()


   }
	return render(request, 'blog/ssb.html',context)


