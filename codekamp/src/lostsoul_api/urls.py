from django.urls import path
from . import views

from rest_framework import routers

app_name = 'lostsoul_api'

router = routers.SimpleRouter()
router.register('articles', views.ArticleViewSet)
router.register('users', views.UserViewSet)

urlpatterns = [
    # path('articles', views.ArticleView.as_view(), name='article_list'),
    # path('articles/<int:id>', views.article_detail, name='article_detail'),
    # path('classviews', views.ArticleView.as_view(), name='article_detail')
]

urlpatterns += router.urls