from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question, Choice
from django.views import generic # 제너릭 뷰 사용

"""
템플릿에 context 를 채워넣어 표현한 결과를 HttpResponse 객체와 함께 돌려주는 구문을
쉽게 표현할 수 있는 단축 기능(shortcuts)
"""
from django.shortcuts import render, get_object_or_404

# Create your views here.
# 22.07.23 add
# view는 인수를 받기 때문에 모양이 조금 다름.

# 뷰가 실제로 뭔가를 하도록 만들기 (def index)
# 질문이 하나인 경우
""" def index(request):
    # return HttpResponse("Hello, world.")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]    
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output) """

 # 질문이 여러 개인 경우 template 활용
'''def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]    
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # return HttpResponse(template.render(context,request))
    return render(request, 'polls/index.html', context)'''

# 404 에러 일으키기 (존재하지 않는 경로에 들어갔을 때 지정한 문구가 뜨도록 함)
'''from django.http import Http404
from django.shortcuts import render

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    #return HttpResponse("You're looking at question %s." % question_id)
    return render(request, 'polls/detail.html', {'question':question})'''

# 404 에러 지름길: get_object_or_404()
# from django.shortcuts import get_object_or_404, render
'''def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})'''

'''
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
'''

#  라디오박스 값 넘기기
'''def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})'''

from django.urls import reverse

def vote(request, question_id):
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


# 아래부터는 제너릭 뷰 사용법
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'