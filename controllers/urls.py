from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse


def redirect_by_name(name='sun_stock_index'):
    return HttpResponseRedirect(reverse(name))


def redirect_by_url(url='/'):
    return redirect(url)
