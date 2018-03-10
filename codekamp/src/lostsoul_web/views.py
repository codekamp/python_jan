from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from pip._vendor import requests

from lostsoul_web.models import Article


def list_articles(request):
    # ip_addr = request.META.get('REMOTE_ADDR')
    ip_addr = '43.225.0.133'

    res = requests.get('http://freegeoip.net/json/' + ip_addr).json()
    user_city = res['city']

    credentials = {'password': 'rajneesh10', 'email': '101.prashant@gmail.com'}
    res = requests.get('https://api.invidz.com/api/authenticate', params=credentials).json()

    token = res['token']
    print(res['user']['first_name'])


    token_header = {'Authorization': 'bearer ' + token}
    videos = requests.get('https://api.invidz.com/api/videos', headers=token_header).json()

    print(videos['data'][3]['title'])
    query = ''
    try:
        query = request.GET['q']
        articles = Article.objects.filter(title__icontains=query)
    except:
        articles = Article.objects.all()

    return render(request, 'list-articles.html', {'my_articles': articles, 'query': query, 'city': user_city})

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
            author = request.user.detail[0].bio
            article = Article.objects.create(title=title, content=content, author=author)
            return redirect('lostsoul_web:article_detail', article.slug)


    return render(request, 'add-article.html', {'title': title, 'content': content, 'error': error})
