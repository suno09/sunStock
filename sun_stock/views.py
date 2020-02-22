from django.http import HttpResponse
from django.views.generic import (View)


# Create your views here.
# The classes are based on CBV


class Index(View):
    def get(self, request):
        return HttpResponse('API index of SunStock Management')
