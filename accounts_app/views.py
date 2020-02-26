from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import (View)
from django.contrib.auth.decorators import login_required

from controllers.enums import AccountState
from controllers.account_controller import account_login


# Create your views here.
# The classes are based on CBV


class Index(LoginRequiredMixin, View):
    # login_url = '/'
    # redirect_field_name = ''

    @staticmethod
    def get(request):
        return HttpResponse('API index of accounts app')


# csrf_exempt = disable csrf
@method_decorator(csrf_exempt, name='dispatch')
class Login(View):
    @staticmethod
    def get(request, *args, **kwargs):
        return JsonResponse({'type': AccountState.DISCONNECTED.value,
                             'message': 'login'})

    @staticmethod
    def post(request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        return account_login(request, username, password)


class LoginTemplate(View):
    @staticmethod
    def get(request, *args, **kwargs):
        return JsonResponse({'type': AccountState.DISCONNECTED.value,
                             'message': 'login'})

    @staticmethod
    def post(request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        return account_login(request, username, password)


class AutoLogin(View):
    @staticmethod
    def get(request, *args, **kwargs):
        if request.session.has_key('username'):
            return JsonResponse({'type': AccountState.CONNECTED.value,
                                 'message': 'auto_login_success'})
        else:
            return JsonResponse({'type': AccountState.DISCONNECTED.value,
                                 'message': 'auto_login_failed'})
