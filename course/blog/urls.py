from django.urls import path
from . import views
from .views import BlogView, BlogDetailView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('teachers/', views.teachers, name='blog-teachers'),
    path('courses/', views.courses, name='blog-courses'),
    path('abroad/', views.abroad, name='blog-abroad'),
    path('contact/', views.contact, name='blog-contact'),
    path('blog/', BlogView.as_view(), name='blog-blog'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post-detail'),
] +   static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 