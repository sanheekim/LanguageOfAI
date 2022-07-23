from .models import Question
from django.http import HttpResponse
# from django.shortcuts import render

# Create your views here.
# 22.07.23 add
# view는 인수를 받기 때문에 모양이 조금 다름.

# 뷰가 실제로 뭔가를 하도록 만들기 (def index)
def index(request):
    # return HttpResponse("Hello, world.")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
