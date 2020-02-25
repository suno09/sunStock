from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import (View, TemplateView)

from controllers.account_controller import account_login, account_logout
from controllers.enums import AccountState

import logging
logger = logging.getLogger(__name__)


# Create your views here.
# The classes are based on CBV


class Index(View):
    @staticmethod
    def get(request, *args, **kwargs):
        if 'session_username' in request.session:
            logger.error("Index View get")
            template_name = 'sun_stock/index.html'

            return render(request, template_name, {})
            # JsonResponse({
            #     'type': AccountState.CONNECTED.value,
            #     'message': 'account not active'
            # })
        else:
            return redirect('/login')

    @staticmethod
    def post(request, *args, **kwargs):
        return JsonResponse({
                'type': AccountState.CONNECTED.value,
                'message': 'account not active'
            })


class Login(View):
    @staticmethod
    def get(request, *args, **kwargs):
        template_name = "sun_stock/login.html"

        return render(request, template_name, {})

    @staticmethod
    def post(request: HttpRequest, *args, **kwargs):
        post_keys = map(lambda k: k.lower(), request.POST.keys())
        if 'login' in post_keys:
            username = request.POST.get('username')
            password = request.POST.get('password')

            response_login: AccountState = account_login(request, username, password)
            if response_login == AccountState.CONNECTED:
                return redirect('/')
                # return JsonResponse({
                #     'type': AccountState.CONNECTED.value,
                #     'message': 'account not active'
                # })
            elif response_login == AccountState.NOT_ACTIVE:
                return JsonResponse({
                    'type': AccountState.NOT_ACTIVE.value,
                    'message': 'account not active'
                })
            else:
                return JsonResponse({
                    'type': AccountState.FAILED.value,
                    'message': 'Invalid account'
                })
        else:
            return JsonResponse({
                'type': AccountState.NOT_ACTIVE.value,
                'message': '404 page'
            })


class Logout(View):
    @staticmethod
    def get(request, *args, **kwargs):
        account_logout(request)

        return redirect('/')
