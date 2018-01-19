from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import TopicForum, SectionForum


class ForumView(ListView):
    """Главная страница форума"""
    template_name = 'sl_forum/forum_start.html'
    model = SectionForum
    context_object_name = 'section'

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['topic'] = TopicForum.objects.all()
        return super(ForumView, self).get_context_data(**kwargs)


def print_kwargs(request, *args, **kwargs):
    s = SectionForum.objects.all()
    l = []
    for foo in s:
        l.append(foo)
    a = print(l)
    return render(request, 'sl_forum/print.html', context={'prin': a})
