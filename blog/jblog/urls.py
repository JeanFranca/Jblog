from django.urls import path
from .views import IndexView, CreateArticleView, ArticleUpdate, ArticleView

app_name="jblog"
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create', CreateArticleView.as_view(), name = "create"),
    path('update/<pk>', ArticleUpdate.as_view(), name = "update"),
    path('view/<pk>', ArticleView.as_view(), name="view"),
]