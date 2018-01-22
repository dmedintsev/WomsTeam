# coding=utf-8
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name="blog"),
    path('single-post/<int:pk>/', views.post_single, name="post_single"),
    path('single-post/<int:pk>/new_comment/', views.new_comment, name="new_comment"),
]
