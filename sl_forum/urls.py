from django.urls import path
from .views import ForumView, TopicCreateView, TopicAllView, TopicOneView

urlpatterns = [
    path('', ForumView.as_view(), name='forum_start'),
    path('topic/<int:pk>/', TopicAllView.as_view(), name='forum_topic_all'),
    path('topic/create/', TopicCreateView.as_view(), name='forum_topic_create'),
    path('topic/one/<int:pk>/', TopicOneView.as_view(), name='forum_topic_one'),
]
