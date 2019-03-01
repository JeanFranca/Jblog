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
    template_name = 'jblog/createArticle.html'
    model = Article
    fields = ('title', 'text')
    success_url = reverse_lazy('jblog:index')

#class ArticleUpdate(UpdateView):
#
#    model = Article
#    fields = ['title', 'text']
#    template_name = 'jblog/editArticle.html'
#    def get_object(self):
#        return get_object_or_404(Article,title=self.kwargs['title'])
#    