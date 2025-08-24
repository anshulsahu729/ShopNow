
# from django.contrib import admin
# from django.urls import path,include
# from .import views

# urlpatterns = [

#     path('', views.blog_list, name='blog_list'),
#     path('create/', views.blog_create, name='blog_create'),
#     path('<slug:slug>/', views.blog_detail, name='blog_detail'),  # cleaner
#     path('<slug:slug>/edit/', views.blog_update, name='blog_update'),
#     path('<slug:slug>/delete/', views.blog_delete, name='blog_delete'),
# ]


from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('create/', views.blog_create, name='blog_create'),
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('<slug:slug>/edit/', views.blog_update, name='blog_update'),
    path('<slug:slug>/delete/', views.blog_delete, name='blog_delete'),
]
