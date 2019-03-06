from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.utils import timezone
from django.views.generic.detail import DetailView

from .models import Article


class IndexView(TemplateView):
    template_name = "jblog/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all().order_by("-published_at")
        return context


class CreateArticleView(LoginRequiredMixin, CreateView):
    template_name = 'jblog/create_article.html'
    model = Article
    fields = ('title', 'text','resume')
    success_url = reverse_lazy('jblog:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Criar Artigo'
        return context


class ArticleUpdate(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ('title', 'text','resume')
    template_name = 'jblog/create_article.html'
    success_url = reverse_lazy('jblog:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editando Artigo <em>{}</em>'.format(
            self.object.title
            )
        return context

class ArticleView(DetailView):
    model = Article
    template_name = 'jblog/view_article.html'
    success_url = reverse_lazy('jblog:index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = timezone.now()
        
        return context