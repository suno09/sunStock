from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import (View, ListView)

from accounts_app.models import UserInfo
from controllers.account_controller import account_login
from controllers.enums import AccountState


# Create your views here.
# The classes are based on CBV


class Index(LoginRequiredMixin, ListView):
    # login_url = '/'
    # redirect_field_name = ''
    context_object_name = 'user_infos'
    model = UserInfo
    template_name = 'accounts_app/account.html'

    def get_context_data(self, **kwargs):
        if self.request.method == 'GET':
            try:
                nshow = int(self.request.GET['nshow'])
                npage = int(self.request.GET['npage'])
            except MultiValueDictKeyError:
                nshow = 10
                npage = 0

            context = super(Index, self).get_context_data(**kwargs)
            # result_set = self.model.objects.raw(
            #     """
            #     select id, username, role,
            #             case role
            #                 when 1 then 'ADMIN'
            #                 when 2 then 'GERANT'
            #                 when 3 then 'VENDEUR'
            #             end as rolen
            #     from accounts_app_userinfo
            #     where active=1 and id_user > 1
            #     order by username limit %s, %s;
            #     """,
            #     [npage * nshow, nshow])
            # result_set = self.model.objects.all()

            context['result_set'] = self.get_queryset()
            context['count'] = self.get_queryset().count()
            context['npage'] = npage
            context['nshow'] = nshow

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
