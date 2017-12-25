from django.urls import path
from . import views

app_name = 'client'
urlpatterns = [
    path('', views.client_profile, name='profile'),
    path('update/', views.update_profile, name='update_profile'),
]
