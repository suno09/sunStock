"""
This file is based on the actions of views.py
"""
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .enums import AccountState

from time import time


def account_login(request, username: str, password: str) -> JsonResponse:
    """
    account_login to login to server
    :param request: request param
    :param username: username of account
    :param password: password of account
    :return: account state type if success or not
    """

    user = authenticate(username=username, password=password)

    if user:
        if user.is_active:
            login(request=request, user=user)
            create_session(request, username)
            return JsonResponse({
                'type': AccountState.CONNECTED.value,
                'message': 'connected'
            })
        else:
            return JsonResponse({
                'type': AccountState.NOT_ACTIVE.value,
                'message': 'account not active'
            })
    else:
        return JsonResponse({
            'type': AccountState.FAILED.value,
            'message': 'Invalid account'
        })


def create_session(request, username):
    """
    Create new session for the user
    :param request: request param
    :param username: username of account
    :return: boolean of successful or failure
    """

    request.session['session_username'] = username
    request.session['session_expire'] = time() + 4 * (60 ** 3)

    return True


def delete_session(request):
    """
    Delete session
    :param request: request param
    :return: boolean of successful
    """
    try:
        del request.session['session_username']
        del request.session['session_expire']
    except KeyError:
        pass

    return True
