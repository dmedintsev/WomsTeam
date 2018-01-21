from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView
from .models import TopicForum, SectionForum, MessageForum, UserForum
from .forms import TopicForm, MessageForm
import markdown


class ForumView(ListView):
    """Главная страница форума выводим Разделы на страницу"""
    template_name = 'sl_forum/forum_start.html'
    model = SectionForum
    context_object_name = 'section'


class TopicAllView(ListView):
    """Выводим темы отсортированные по данному разделу"""
    template_name = 'sl_forum/forum_topic_all.html'
    context_object_name = 'topic'

    def get_queryset(self):
        topics = TopicForum.objects.filter(section=self.kwargs['pk'])
        for topic in topics:
            topic.text = markdown.markdown(topic.text,)
        return topics


class TopicOneView(TemplateView):
    """Выводим одну тему с описанием"""
    template_name = 'sl_forum/forum_topic_one.html'

    def get_context_data(self, **kwargs):
        kwargs['topic'] = TopicForum.objects.get(pk=kwargs['pk'])
        kwargs['message'] = MessageForum.objects.filter(topic=kwargs['pk']).order_by('created')
        kwargs['form'] = MessageForm()
        kwargs['views'] = UserForum.objects.get(pk=kwargs['pk'])
        return super(TopicOneView, self).get_context_data(**kwargs)

    def post(self, request, **kwargs):
        if request.method == 'POST':
            form = MessageForm(request.POST)
            if form.is_valid():
                user = request.user
                topic = TopicForum.objects.get(pk=kwargs['pk'])
                text = form.cleaned_data['text']
                new_record = MessageForum(user=user, topic=topic, text=text)
                new_record.save()
                for user in UserForum.objects.filter():
                    user.user = request.user
                    user.views += 1
                    user.save(update_fields=['user', 'views'])
                return HttpResponseRedirect(reverse('forum_topic_one', args=[str(topic.pk)]))


class TopicCreateView(CreateView):
    """Создание темы на форуме"""
    template_name = 'sl_forum/forum_topic_create.html'
    model = TopicForum
    form_class = TopicForm
    context_object_name = 'topic'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse('forum_topic_one', args=[str(obj.pk)]))
