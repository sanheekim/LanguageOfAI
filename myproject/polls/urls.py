# 22.07.23 view를 호출하기 위함.

from django.urls import path

from . import views
app_name = 'polls' # myproject/urls.py에 namespace = 'polls' 추가할 때 필요함.
urlpatterns = [
    # ex: /polls/
    path('',views.IndexView.as_view(), name='index'),
    # ex: /polls/5
    #위 url에 /specifics/를 추가
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

''' 제너릭 뷰 사용하기 전 코드
    # path('',views.index, name='index'),
    #path('<int:question_id>/',views.detail,name='detail'),
     # path('<int:question_id>/detail/', views.detail, name='results'),
    # path('<int:question_id>/results/', views.results, name='results'),

    # 제너릭 뷰 사용법 : polls/views.py에서 참고
'''