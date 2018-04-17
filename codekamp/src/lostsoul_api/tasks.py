from __future__ import absolute_import, unicode_literals
from celery import shared_task
from pip._vendor import requests



# @shared_task
# def analyze_tweet(id, age):
#     def delay():
#
#     tweet = Tweet.objects.find(id)
#
#     res = requests.get("https://api.perspective.com/analyze?text="+tweet.text + "&age="+age).json()
#
#     tweet.rating = res.rating
#     tweet.save()

@shared_task
def analyze_tweet(id):
    print("analyzing the tweet id: ", id)