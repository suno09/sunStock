import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.views.generic import (View)

from controllers.account_controller import account_login, account_logout
from controllers.enums import AccountState
from controllers.urls import redirect_by_name

logger = logging.getLogger(__name__)


# Create your views here.
# The classes are based on CBV


class Index(LoginRequiredMixin, View):
    @staticmethod
    def get(request, *args, **kwargs):
        request.session['cpage'] = 'index'
        template_name = 'sun_stock/index.html'

        return render(request, template_name, {})

# csrf_exempt = disable csrf
# @method_decorator(csrf_exempt, name='dispatch')


class Login(View):
    @staticmethod
    def get(request, *args, **kwargs):
        request.session['cpage'] = 'login'
        template_name = "sun_stock/login.html"

        return render(request, template_name, {})

    @staticmethod
    def post(request: HttpRequest, *args, **kwargs):
        post_keys = map(lambda k: k.lower(), request.POST.keys())

        username = request.POST.get('username')
        password = request.POST.get('password')

        response_login: AccountState = account_login(request, username, password)

        # Login in html page
        if 'login_template' in post_keys:
            if response_login == AccountState.CONNECTED:
                return redirect_by_name()
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

        return redirect_by_name()
