from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from lostsoul_web.models import Article, Author


def list_articles(request):
    query = ''
    try:
        query = request.GET['q']
        articles = Article.objects.filter(title__icontains=query)
    except:
        articles = Article.objects.all()

    return render(request, 'list-articles.html', {'my_articles': articles, 'query': query})

def get_article(request, my_slug):
    article = Article.objects.get(slug=my_slug)
    return render(request, 'get-article.html', {'article': article})

@login_required()
def add_artile(request):
    title=''
    content=''
    error = False

    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']

        if len(title) > 30:
            error = True
        else:
            author = Author.objects.get(id=1)  # get logged in author
            article = Article.objects.create(title=title, content=content, author=author)
            return redirect('lostsoul_web:article_detail', article.slug)


    return render(request, 'add-article.html', {'title': title, 'content': content, 'error': error})
