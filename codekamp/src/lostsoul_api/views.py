from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views import View
from pip._vendor import requests
from rest_framework import mixins, status
from rest_framework.decorators import api_view, detail_route, list_route
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet, GenericViewSet

from lostsoul_api.serialize import ArticleSerializer, DetailedArticleSerializer, UserSerializer, YouTubeSerializer

from lostsoul_web.models import Article


# @api_view(['GET', 'DELTE', 'PUT', 'PATCH'])
# def article_detail(request, id):
#     article = Article.objects.get(id=id)
#
#     return Response(DetailedArticleSerializer(article, many=False).data)
#
#
class ArticleView(APIView):

    def get(self, request):
        articles = Article.objects.all()
        searilizer = ArticleSerializer(articles, many=True)
        return Response(searilizer.data)

    def post(self, request):
        serialiser = DetailedArticleSerializer(data=request.data, many=True)

        serialiser.is_valid(raise_exception=True)
        articles = serialiser.save(xyz=request.user)
        # article = Article()
        # article.title = serialiser.validated_data['title']  # request.data['article_title']
        # article.content = serialiser.validated_data['content']
        # article.author = request.user
        # article.save()

        return Response(DetailedArticleSerializer(articles[0], many=False).data)
    # else:
    #     return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)


# class ArticleViewSet(ModelViewSet):
#     queryset = Article.objects.all()
#
#     def get_serializer_class(self):
#         if(self.action == 'list'):
#             return ArticleSerializer
#         else:
#             return DetailedArticleSerializer
#
# def get_queryset(self):
#     user = self.request.user
#     if(user.isAdmin()):
#         return self.queryset
#     else:
#         return self.queryset.filter(author=user)


# @detail_route(methods=['POST'])
# def copy(self, request, pk):
#     existing = self.queryset.get(pk=pk)
#     existing.id = None
#     existing.slug += '_2'
#     existing.save()
#     return Response({'method':existing.id})


class UserViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class YouTubeApiView(APIView):
    def get(self, request, query):
        data = {"key": "AIzaSyBmdVLdL9w8ah-UUEar6pQmh4GjW5JMQlI", "part": "snippet", "q": query, format: "json"}

        res = requests.get("https://www.googleapis.com/youtube/v3/search", params=data).json()

        output = YouTubeSerializer(res['items'], many=True).data
        return Response(output)
