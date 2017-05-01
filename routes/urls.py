from django.conf.urls import url
from django.conf.urls import include

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic


from . import views

app_name = 'routes'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.RoutesView.as_view(), name='routes'),
#    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
#    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]