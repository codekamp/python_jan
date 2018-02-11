from django.urls import path
from . import views

my_urls = [
    path('articles', views.list_articles),
    path('articles/<str:my_slug>', views.get_article),
]