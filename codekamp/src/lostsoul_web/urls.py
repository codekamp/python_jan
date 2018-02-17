from django.urls import path
from . import views

app_name = 'lostsoul_web'

urlpatterns = [
    path('articles', views.list_articles, name='article_list'),
    path('articles/add', views.add_artile, name='add_new_article'),
    path('articles/<str:my_slug>', views.get_article, name='article_detail'),
]