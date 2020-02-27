from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import (View, ListView)

from accounts_app.models import UserInfo
from controllers.enums import AccountState
from controllers.account_controller import account_login


# Create your views here.
# The classes are based on CBV


class Index(LoginRequiredMixin, ListView):
    # login_url = '/'
    # redirect_field_name = ''
    context_object_name = 'user_infos'
    model = UserInfo

    def get_context_data(self, **kwargs):
        if self.request.method == 'GET':
            context = super(Index, self).get_context_data(**kwargs)
            filter_ = UserInfo.objects.filter()

            context['count'] = self.get_queryset().count()
            return context


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
