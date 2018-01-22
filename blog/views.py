from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from blog.forms import CommentForm
from .models import Post, Comment


def post_list(request):
    """ Список новостей
    """
    post = Post.objects.all()
    return render(request, 'blog/post_list.html', {"posts": post})


def post_single(request, pk):
    """ Полная статья
    """
    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post=post.pk)
    return render(request, "blog/post_single.html", {"post": post, "comments": comments})


@csrf_exempt
def new_comment(request, pk):
    """Создание нового комментария к статье
    """
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            tt = form.save(commit=False)
            tt.post = Post.objects.get(pk=pk)
            tt.save()
            return redirect(post_single, pk)
    return render(request, "blog/new_comment.html", {"form": CommentForm})
