from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from urlapp.views import RedirectView, MainView


urlpatterns = [
    url(r'^(?P<short_id>\w{6})$', RedirectView.as_view(), name='redirect'),
    url(r'^$', MainView.as_view(), name='makeshort'),
    ]