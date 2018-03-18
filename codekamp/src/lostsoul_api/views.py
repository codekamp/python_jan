from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet

from lostsoul_api.serialize import ArticleSerializer, DetailedArticleSerializer, UserSerializer

from lostsoul_web.models import Article


# @api_view(['GET', 'DELTE', 'PUT', 'PATCH'])
# def article_detail(request, id):
#     article = Article.objects.get(id=id)
#
#     return Response(DetailedArticleSerializer(article, many=False).data)
#
#
# class ArticleView(APIView):
#
#     def get(self, request):
#         articles = Article.objects.all()
#         json = ArticleSerializer(articles, many=True)
#         return Response(json.data)
#
#     def post(self, request):
#         serialiser = DetailedArticleSerializer(data=request.data, many=False)
#
#         if (serialiser.is_valid()):
#             title = request.data['article_title']
#             content = request.data['content']
#             article = Article.objects.create(title=title, content=content, author=request.user)
#             return Response(DetailedArticleSerializer(article, many=False).data)
#         else:
#             return Response(serialiser.errors, status=404)


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
