from django.urls import re_path
from .views import *

app_name = 'basic_app'

urlpatterns = [
    re_path(r'^$', Index.as_view(), name="accounts_app_index"),
    # re_path(r'^login_api$', Login.as_view(), name="accounts_app_login"),
    # re_path(r'^login$', Login.as_view(), name="accounts_app_login_template"),
    # re_path(r'^(?P<pk>\d+)/$', SchoolDetailView.as_view(), name="detail"),
    # re_path(r'^create/$', SchoolCreateView.as_view(), name="create"),
    # re_path(r'^update/(?P<pk>\d+)/$', SchoolUpdateView.as_view(), name="update"),
    # re_path(r'^delete/(?P<pk>\d+)/$', SchoolDeleteView.as_view(), name="delete"),
]
