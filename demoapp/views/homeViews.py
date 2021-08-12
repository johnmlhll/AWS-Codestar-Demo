import os
from django.shortcuts import render
from django.views.generic.base import TemplateView



# Create your views here.
class HomePageView(TemplateView):

    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        service_update = os.popen("uptime").read()
        uptime = {'service_update':service_update}
        return render(request, self.template_name, context=uptime)