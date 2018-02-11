from django.shortcuts import render

from lostsoul_web.models import Article


def list_articles(request):
    articles = Article.objects.all()
    return render(request, 'list-articles.html', {'my_articles': articles})

def get_article(request, my_slug):
    article = Article.objects.get(slug=my_slug)
    return render(request, 'get-article.html', {'article': article})