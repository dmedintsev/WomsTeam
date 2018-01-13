from django.urls import path
from .views import ForumView, print_kwargs

urlpatterns = [
    path('', ForumView.as_view(), name='forum_start'),
    path('test/', print_kwargs, name='forum_start'),
]
