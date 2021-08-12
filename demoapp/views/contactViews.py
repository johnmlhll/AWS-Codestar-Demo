from django.shortcuts import render
from django.views.generic.base import TemplateView


# Contact View
class ContactPageView(TemplateView):
    contact_name = 'contact.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.contact_name, context=None)
