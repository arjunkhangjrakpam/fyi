from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .models import Post_rimc
from .models import Post_ssb

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.dates import YearArchiveView
	

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


class PostListView(ListView):
	model = Post
	template_name = 'blog/nda_na.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']

class Post_rimcListView(ListView):
	model = Post_rimc
	template_name = 'blog/rimc.html'
	context_object_name = 'post_rimc'
	ordering = ['-date_posted']	

class Post_ssbListView(ListView):
	model = Post_ssb
	template_name = 'blog/ssb.html'
	context_object_name = 'post_ssb'
	ordering = ['-date_posted']	


class PostDetailView(DetailView):
	model = Post

class Post_rimcDetailView(DetailView):
	model = Post_rimc

class Post_ssbDetailView(DetailView):
	model = Post_ssb





class PostCreateView(CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class Post_rimcCreateView(CreateView):
	model = Post_rimc
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class Post_ssbCreateView(CreateView):
	model = Post_ssb
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)




class PostUpdateView(UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class Post_rimcUpdateView(UserPassesTestMixin, UpdateView):
	model = Post_rimc
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


	def test_func(self):
		post_rimc = self.get_object()
		if self.request.user == post_rimc.author:
			return True
		return False

class Post_ssbUpdateView(UserPassesTestMixin, UpdateView):
	model = Post_ssb
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


	def test_func(self):
		post_ssb = self.get_object()
		if self.request.user == post_ssb.author:
			return True
		return False




	
class PostDeleteView(UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'
	fields = ['title', 'content']

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False
	
class Post_rimcDeleteView(UserPassesTestMixin, DeleteView):
	model = Post_rimc
	success_url = '/'
	fields = ['title', 'content']

	def test_func(self):
		post_rimc = self.get_object()
		if self.request.user == post_rimc.author:
			return True
		return False
	
class Post_ssbDeleteView(UserPassesTestMixin, DeleteView):
	model = Post_ssb
	success_url = '/'
	fields = ['title', 'content']

	def test_func(self):
		post_ssb = self.get_object()
		if self.request.user == post_ssb.author:
			return True
		return False
	



class PostYearArchiveView(YearArchiveView):
	queryset = Post.objects.all()
	date_field = "date_posted"
	make_object_list = True
	allow_future = True

class Post_rimcYearArchiveView(YearArchiveView):
	queryset = Post_rimc.objects.all()
	date_field = "date_posted"
	make_object_list = True
	allow_future = True

class Post_ssbYearArchiveView(YearArchiveView):
	queryset = Post_ssb.objects.all()
	date_field = "date_posted"
	make_object_list = True
	allow_future = True



def about(request):
	return render(request, 'blog/about.html')