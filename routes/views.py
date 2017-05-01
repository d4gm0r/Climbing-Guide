from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic


from .models import Route, Area

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'routes/index.html'
    context_object_name = 'latest_areas_list'

    def get_queryset(self):
        return Area.objects.order_by('areas_text')


class RoutesView(generic.DetailView):
    model = Area
    template_name = 'routes/routes.html'
