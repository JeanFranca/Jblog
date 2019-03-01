from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView 
from django.views.generic.edit import CreateView, CreateView, UpdateView
from .models import Article

class IndexView(TemplateView):
    template_name = "jblog/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all().order_by("-published_at")
        return context

class CreateArticleView(CreateView):
    template_name = 'jblog/create_article.html'
    model = Article
    fields = ('title', 'text')
    success_url = reverse_lazy('jblog:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Criar Artigo'
        return context 

class ArticleUpdate(UpdateView):
    model = Article
    fields = ('title', 'text')
    template_name = 'jblog/create_article.html'
    success_url = reverse_lazy('jblog:index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editando Artigo <em>{}</em>'.format(self.object.title)
        return context