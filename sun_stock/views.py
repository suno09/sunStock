from django.http import HttpResponse
from django.views.generic import (View, TemplateView)
from django.shortcuts import render


# Create your views here.
# The classes are based on CBV


class Index(View):
    @staticmethod
    def get(request, *args, **kwargs):
        # template_name = 'sun_stock/login.html'
        #
        # return render(request, template_name, {})
        if request.session.has_key('username_session'):
            template_name = 'sun_stock/index.html'
        else:
            template_name = 'sun_stock/login.html'

        return render(request, template_name, {})
