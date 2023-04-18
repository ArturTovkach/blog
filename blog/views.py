from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import News
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/'
    template_name = 'blog/delete-news.html'

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        else:
            return False


class ShowNewsView(ListView):
    model = News
    template_name = 'blog/home.html'
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        ctx = super(ShowNewsView, self).get_context_data(**kwargs)

        ctx['title'] = 'Главная страница сайта'
        return ctx

class NewsDetailView(DetailView):
    model = News
    template_name = 'blog/news-detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwards):
        ctx = super(NewsDetailView, self).get_context_data(**kwards)

        ctx['title'] = News.objects.get(pk=self.kwargs['pk'])
        return ctx

class UpdateNewsView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = News
    template_name = 'blog/create-news.html'

    fields = ['title', 'text']

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        else:
            return False

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)




    def get_context_data(self, **kwargs):
        ctx = super(UpdateNewsView, self).get_context_data(**kwargs)

        ctx['title'] = 'Обновление статьи'
        ctx['btn_text'] = 'Обновить статью'
        return ctx


class CreateNewsView(CreateView, LoginRequiredMixin):
    model = News
    template_name = 'blog/create-news.html'

    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.avtor=self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(CreateNewsView, self).get_context_data(**kwargs)

        ctx['title'] = 'Добавление статьи'
        ctx['btn_text'] = 'Добавить статью'
        return ctx

def contacti(request):
    return render(request, 'blog/contacti.html', {'title':'Страница контакты'})


class UserAllNewsView(ListView):
    model = News
    template_name = 'blog/user_news.html'
    context_object_name = 'news'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return News.objects.filter(avtor = user).order_by('-date')

    def get_context_data(self, **kwargs):
        ctx = super(UserAllNewsView, self).get_context_data(**kwargs)

        ctx['title'] = f'Статьи от пользователя { self.kwargs.get("username") }'
        return ctx