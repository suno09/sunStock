from django.contrib.auth.models import User
from django.test import Client
from accounts_app.models import Rank, UserInfo


def create_user(username, password, rank=Rank.ADMIN):
    user = User.objects.create_user(username=username, password=password)
    user.save()

    user_info = UserInfo(user=user, rank=rank)
    user_info.save()

    return user_info


def send_request(url, params, post=False):
    url = 'http://127.0.0.1:8000' + url
    c = Client()
    if not post:
        return c.get(url)
    else:
        return c.post(url, params)
