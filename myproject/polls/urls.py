# 22.07.23 view를 호출하기 위함.

from django.urls import path

from . import views
app_name = 'polls' # myproject/urls.py에 namespace = 'polls' 추가할 때 필요함.
urlpatterns = [
    # ex: /polls/
    path('',views.index, name='index'),
    # ex: /polls/5
    #path('<int:question_id>/',views.detail,name='detail'),
    #위 url에 /specifics/를 추가
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]