from django.http import HttpResponse


def get_profile(request, user_id):
    users = [{'name': 'Amit', 'about': 'I am amit'}, {'name': 'Sumit', 'about': 'I love programming'}]
    return HttpResponse(users[user_id - 1]['name'])