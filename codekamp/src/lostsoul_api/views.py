from rest_framework.decorators import api_view
from rest_framework.response import Response

from lostsoul_api.serialize import ArticleSerializer, DetailedArticleSerializer

from lostsoul_web.models import Article


@api_view(['GET', 'POST'])
def get_articles(request):
    articles = Article.objects.all()

    json = ArticleSerializer(articles, many=True)

    return Response(json.data)

@api_view(['GET', 'DELTE', 'PUT', 'PATCH'])
def article_detail(request, id):
    article  = Article.objects.get(id=id)

    return Response(DetailedArticleSerializer(article, many=False).data)

