from django.http import JsonResponse


def get_profile(request, user_id):
    users = [{'name': 'Amit', 'about': 'I am amit'}, {'name': 'Sumit', 'about': 'I love programming'}]
    return JsonResponse({'data': users})


# api/users
# api/users/<user_id>