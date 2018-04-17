from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from pip._vendor import requests

from lostsoul_web.models import Article


def list_articles(request):
    state = get_random_string(32)
    user_city = 'Ghaziabad'

    print(request.user.id)
    cache.set(state, request.user.id, 6000)


    requests.post("https://api.twitter.com/oauth/request_token")

    # ip_addr = request.META.get('REMOTE_ADDR')
    # ip_addr = '43.225.0.133'
    #
    # res = requests.get('http://freegeoip.net/json/' + ip_addr).json()
    # user_city = res['city']
    #
    # credentials = {'password': 'rajneesh10', 'email': '101.prashant@gmail.com'}
    # res = requests.get('https://api.invidz.com/api/authenticate', params=credentials).json()
    #
    # token = res['token']
    # print(res['user']['first_name'])
    #
    #
    # token_header = {'Authorization': 'bearer ' + token}
    # videos = requests.get('https://api.invidz.com/api/videos', headers=token_header).json()
    #
    # print(videos['data'][3]['title'])
    query = ''
    try:
        query = request.GET['q']
        articles = Article.objects.filter(title__icontains=query)
    except:
        articles = Article.objects.all()

    return render(request, 'list-articles.html',
                  {'my_articles': articles, 'query': query, 'city': user_city, 'state': state})


def get_article(request, my_slug):
    article = Article.objects.get(slug=my_slug)
    return render(request, 'get-article.html', {'article': article})


@login_required()
def add_artile(request):
    title = ''
    content = ''
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


def facebook_oauth(request):
    grant = request.GET['code']
    state = request.GET['state']

    user_id = cache.get(state)

    if (user_id == request.user.id):
        client_secret = ''
        data = {'client_id': '', 'redirect_uri': 'http://localhost:8080/oauth/facebook',
                'client_secret': client_secret, 'code': grant}
        res = requests.get(
            'https://graph.facebook.com/v2.12/oauth/access_token', params=data).json()
        request.user.facebook_token = res['access_token']
        request.user.save()

        print(res['access_token'])

        return redirect('lostsoul_web:add_new_article')

def github_oauth(request):
    grant = request.GET['code']
    state = request.GET['state']

    user_id = cache.get(state)

    if (user_id == request.user.id):
        client_id = '99483968851edaa50f7f'
        client_secret = '65737905e37e46bceae4cb8d575971b57db1d0e7'
        data = {'client_id': client_id, 'redirect_uri': 'http://localhost:8080/oauth/github',
                'client_secret': client_secret, 'code': grant}

        headers = {'Accept': 'application/json'}
        res = requests.post(
            'https://github.com/login/oauth/access_token', params=data, headers=headers).json()
        request.user.facebook_token = res['access_token']
        request.user.save()

        emailRes = requests.get('https://api.github.com/user/emails?access_token=' + res['access_token'])
        print(emailRes)
        return redirect('lostsoul_web:add_new_article')
