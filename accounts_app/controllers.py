"""
This file is based on the actions of views.py
"""
from django.contrib.auth import authenticate, login
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
            return AccountState.CONNECTED
        else:
            return AccountState.NOT_ACTIVE
    else:
        return AccountState.FAILED
