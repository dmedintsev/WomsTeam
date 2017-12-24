from django.shortcuts import render
from .models import Post


def post_list(request):
    """ Список новостей
    """
    post = Post.objects.all()
    return render(request, 'blog/post_list.html', {"posts": post})


def post_single(request, pk):
    """ Полная статья
    """
    post = Post.objects.get(id=pk)
    return render(request, "blog/post_single.html", {"post": post})
