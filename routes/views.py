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
        return Area.objects.order_by('-pub_date')


class RoutesView(generic.DetailView):
    model = Area
    template_name = 'routes/routes.html'


#class ResultsView(generic.DetailView):
#    model = Areas
#    template_name = 'routes/results.html'


"""def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'routes/detail.html', {
            'question': question,
            'error_message': "No choice was selected.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('routes:results', args=(question.id,)))"""