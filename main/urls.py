from django.urls import path
from . import views

urlpatterns = [
    path('', views.home.as_view(),  name='home'),
    path('about', views.about,  name='about'),
    path('gallery', views.gallery,  name='gallery'),
    path('grow_deeper', views.grow_deeper.as_view(),  name='grow_deeper'),
    path('admin_tutorials', views.admin_tutorials,  name='admin_tutorials'),
]
