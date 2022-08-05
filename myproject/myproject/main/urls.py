# 22.07.23 view를 호출하기 위함.

from django.urls import path

from . import views
app_name = 'main' # myproject/urls.py에 namespace = 'main' 추가할 때 필요함.
urlpatterns = [
    # 개인 프로젝트 화면 ex: /main/
    path('', views.main, name='main'),
]