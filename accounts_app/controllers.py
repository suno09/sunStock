"""
This file is based on the actions of views.py
"""
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .enums import AccountState


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

    return True


def delete_session(request):
    """
    Delete session
    :param request: request param
    :return: boolean of successful
    """
    try:
        del request.session['session_username']
    except KeyError:
        pass

    return True
