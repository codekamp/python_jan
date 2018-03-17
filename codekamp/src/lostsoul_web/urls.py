from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'lostsoul_web'

urlpatterns = [
    path('articles', views.list_articles, name='article_list'),
    path('articles/add', views.add_artile, name='add_new_article'),
    path('oauth/facebook', views.facebook_oauth, name='facebook_oauth'),
    path('articles/<str:my_slug>', views.get_article, name='article_detail'),
    path('auth/login', auth_views.LoginView.as_view(), name='login_page')
]