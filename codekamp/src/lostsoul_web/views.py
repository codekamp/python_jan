from django.shortcuts import render

def get_profile(request, user_id):
    users = [{'name': 'Amit', 'about': 'I am amit'}, {'name': 'Sumit', 'about': 'I love programming'}]

    user = users[user_id - 1]
    return render(request, 'profile.html', {'users': users})