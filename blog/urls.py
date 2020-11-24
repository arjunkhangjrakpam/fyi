from django.urls import path
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import PostListView, Post_rimcListView, Post_ssbListView
from .views import PostDetailView, Post_rimcDetailView, Post_ssbDetailView
from .views import PostCreateView, Post_rimcCreateView, Post_ssbCreateView
from .views import PostUpdateView, Post_rimcUpdateView, Post_ssbUpdateView
from .views import PostDeleteView, Post_rimcDeleteView, Post_ssbDeleteView
from .views import PostYearArchiveView, Post_rimcYearArchiveView, Post_ssbYearArchiveView
from django.views.generic.dates import ArchiveIndexView
from blog.models import Post
from blog.models import Post_rimc
from blog.models import Post_ssb
from .views import about

urlpatterns = [
	path('', views.index, name='index'),
	path('nda_na', PostListView.as_view(), name='nda_na'),
	path('rimc', Post_rimcListView.as_view(), name='rimc'),
	path('ssb', Post_ssbListView.as_view(), name='ssb'),
	path('register/', user_views.register, name='register'),
	path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
	path('profile/', user_views.profile, name='profile'),
	path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
	path('post_rimc/<int:pk>/', Post_rimcDetailView.as_view(), name='post_rimc-detail'),
	path('post_ssb/<int:pk>/', Post_ssbDetailView.as_view(), name='post_ssb-detail'),

	path('post/new/', PostCreateView.as_view(), name='post-create'),
	path('post_rimc/new/', Post_rimcCreateView.as_view(), name='post_rimc-create'),
	path('post_ssb/new/', Post_ssbCreateView.as_view(), name='post_ssb-create'),

	path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
	path('post_rimc/<int:pk>/update', Post_rimcUpdateView.as_view(), name='post_rimc-update'),
	path('post_ssb/<int:pk>/update', Post_ssbUpdateView.as_view(), name='post_ssb-update'),

	path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
	path('post_rimc/<int:pk>/delete', Post_rimcDeleteView.as_view(), name='post_rimc-delete'),
	path('post_ssb/<int:pk>/delete', Post_ssbDeleteView.as_view(), name='post_ssb-delete'),
	
	path('archive/', ArchiveIndexView.as_view(model=Post, date_field="date_posted"), name='post_archive'),
	path('archive_rimc/', ArchiveIndexView.as_view(model=Post_rimc, date_field="date_posted"), name='post_rimc_archive'),
	path('archive_ssb/', ArchiveIndexView.as_view(model=Post_ssb, date_field="date_posted"), name='post_ssb_archive'),
	
	path('archive/<int:year>/', PostYearArchiveView.as_view(), name='post_year_archive'),
	path('archive_rimc/<int:year>/', Post_rimcYearArchiveView.as_view(), name='post_rimc_year_archive'),
	path('archive_ssb/<int:year>/', Post_ssbYearArchiveView.as_view(), name='post_rimc_year_archive'),
    
    path('about/', views.about, name='about'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
