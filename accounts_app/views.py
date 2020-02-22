from django.http import HttpResponse, JsonResponse
from django.views.generic import (View)

from .controllers import account_login
from .enums import AccountState


# Create your views here.
# The classes are based on CBV


class Index(View):
    @staticmethod
    def get(request):
        return HttpResponse('API index of accounts app')


class Login(View):
    @staticmethod
    def get(request, *args, **kwargs):
        return JsonResponse({'type': AccountState.DISCONNECTED.value,
                             'message': 'login'})

    @staticmethod
    def post(request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        account_state = account_login(request, username, password)

        if account_state != AccountState.FAILED:
            if account_state == AccountState.CONNECTED:
                return JsonResponse({
                    'type': account_state.value,
                    'message': 'connected'
                })
            else:
                return JsonResponse({
                    'type': account_state.value,
                    'message': 'account not active'
                })
        else:
            return JsonResponse({
                'type': account_state.value,
                'message': 'Invalid account'
            })
