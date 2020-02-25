"""
This file is based on the actions of views.py
"""
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from .enums import AccountState


def account_login(request, username: str, password: str) -> AccountState:
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
            return AccountState.CONNECTED
        else:
            return AccountState.NOT_ACTIVE
    else:
        return AccountState.FAILED


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


def check_session():
    pass


def account_logout(request):
    logout(request)
    delete_session(request)
