# helloworld/urls.py
from django.conf.urls import url
from demoapp.views.homeViews import HomePageView
from demoapp.views.contactViews import ContactPageView

urlpatterns = [
    url(r'^$', HomePageView.as_view()),
    url(r'^contact/$', ContactPageView.as_view()),
]
