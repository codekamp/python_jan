from django.urls import path
from . import views

from rest_framework.authtoken import views as rfviews

from rest_framework import routers

app_name = 'lostsoul_api'


router = routers.SimpleRouter()
# router.register('articles', views.ArticleViewSet)
# router.register('users', views.UserViewSet)

urlpatterns = [
    # path('articles', views.article_detail, name='article_list'),
    # path('articles/<int:id>', views.article_detail, name='article_detail'),
    # path('articles/<int:id>/copy', views.article_detail, name='article_detail'),
    path('articles', views.ArticleView.as_view(), name='article_detail'),
    path('youtube/search/<str:query>', views.YouTubeApiView.as_view(), name='youtube_search'),
    path('authenticate', rfviews.obtain_auth_token)
]

urlpatterns += router.urls