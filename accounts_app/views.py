from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import (View)

from .controllers import account_login
from .enums import AccountState


# Create your views here.
# The classes are based on CBV


class Index(View):
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
