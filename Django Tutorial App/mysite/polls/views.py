from django.shortcuts import render
from .models import Choice, Question
#from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.views import generic 
"""
def index(request):
	latest_ques_list = Question.objects.order_by('-pub_date')[:5]
	#template = loader.get_template('polls/index.html')
	context = {
		'latest_ques_list': latest_ques_list,
	}
	#output = ', '.join([q.question_text for q in latest_ques_list])
	#return HttpResponse(template.render(context,request))

	#shortcut
	return render(request,'polls/index.html',context)

def detail(request, question_id):
	#return HttpResponse("You are looking at question %s." % question_id)
	
	'''try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist!")
	return render(request,'polls/detail.html', {'question':question})
	'''
	question = get_object_or_404(Question, pk=question_id)
	return render(request,'polls/detail.html',{'question':question})

def results(request, question_id):
	#return HttpResponse("You are looking at the results of %s." % question_id)
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question' : question})
"""

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_ques_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


def vote(request, question_id):
	#return HttpResponse("You are voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
