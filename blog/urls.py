from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('create/new/', views.blog_create, name='blog_create'),
    path('update/<slug:slug>/', views.blog_update, name='blog_update'),
    path('delete/<slug:slug>/', views.blog_delete, name='blog_delete'),
]
