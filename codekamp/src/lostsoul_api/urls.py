from django.urls import path
from . import views

app_name = 'lostsoul_api'

urlpatterns = [
    path('articles', views.get_articles, name='article_list'),
    path('articles/<int:id>', views.article_detail, name='article_detail')
]