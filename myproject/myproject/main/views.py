from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question, Choice
from django.views import generic # 제너릭 뷰 사용
from django.shortcuts import render, get_object_or_404

# Create your views here.
# 22.07.23 add
# view는 인수를 받기 때문에 모양이 조금 다름.

# 뷰가 실제로 뭔가를 하도록 만들기 (def main)
 # 질문이 여러 개인 경우 template 활용
def main(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]    
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # return HttpResponse(template.render(context,request))
    return render(request, 'polls/index.html', context)