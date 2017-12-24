# coding=utf-8
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list),
    path('single-post/<int:pk>/', views.post_single, name="post_single"),
]
