from django.http import HttpResponse
from django.template import loader 

from .models import Question

"""
템플릿에 context 를 채워넣어 표현한 결과를 HttpResponse 객체와 함께 돌려주는 구문을
쉽게 표현할 수 있는 단축 기능(shortcuts)
"""
from django.shortcuts import render

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
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]    
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # return HttpResponse(template.render(context,request))
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
