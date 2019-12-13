
from django.http import HttpResponse

from .models import Question

from django.template import loader

from django.shortcuts import get_object_or_404, render

# def index(request):
#     # latest_question_list = Question.objects.all()
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)




 
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('poll/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'poll/index.html', context)

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'poll/detail.html', {'question': question})
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question, 
    }
    #pint("\n\n\n test = recent",qustion.was_publishd_recently(),"\n\n\n\")
    return render(request, 'poll/detail.html', context )

 
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
 
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)