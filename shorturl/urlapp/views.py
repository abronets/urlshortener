import random
import string

from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from django.views import View
from django.views.generic import CreateView, TemplateView

from urlapp.forms import UrlForm
from urlapp.models import Url


def get_short_code():
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    while True:
        short_id = ''.join(random.choice(char) for x in range(6))
        try:
            temp = Url.objects.get(pk=short_id)
        except:
            return short_id


class RedirectView(TemplateView):
    def get(self, request, *args, **kwargs):
        url = get_object_or_404(Url, pk=kwargs['short_id'])  # get object, if not        found return 404 error
        return HttpResponseRedirect(url.long_url)


class MainView(CreateView):
    model = Url
    template_name = 'index.html'
    form_class = UrlForm
    success_url = '/'

    def form_valid(self, form):
        new_form = form.save(commit=False)
        new_form.short_id = get_short_code()
        new_form.short_url = settings.SITE_URL + '/' + new_form.short_id
        new_form.save()
        return HttpResponseRedirect('/')

    def get_context_data(self, **kwargs):
        kwargs['urls'] = Url.objects.order_by()
        return super(MainView, self).get_context_data(**kwargs)