# Language Of AI

### 인공지능 자연어처리에 대한 관심
웹 개발 분야에서 커리어를 즐겁게 쌓아가고 있지만 개발자가 된 이유 중 하나인 자연어처리에 대한 갈증이 여전해서, 관련 사이드 프로젝트를 진행 중입니다.

### Note
1. vscode terminal을 power shell에서 cmd로 바꿔야 가상환경 접속 가능함.
2. virtualenv venv 로 폴더 생성.
3. cd venv
cd Scripts
activate.bat
을 입력하면 가상환경에 접속됨.
이후 pip install django 로 장고 설치함.
4. django-admin startproject myproject 으로 django project 생성.
(이렇게 해서 생성된 상위폴더와 하위폴더명은 myproject로 일치함. 헷갈려도 폴더명 수정하지 말 것. 수정하면 8번 과정에서 ModuleNotFound 오류 남.)
5. (가상환경 접속해서 cd myproject 한 상태)
py manage.py startapp polls로 앱 생성
6. gitforwindows.org 에서 git 설치
7. git bash 열기
    * 이 프로젝트의 myproject 폴더까지 이동(명령어 cd)
    * git init
    * git add .
    * git commit -m "커밋메세지"
    * i → 눌러야 리눅스 터미널에서 글자 작성이 가능함.
    * :wq → 저장됨.
    * git log → 저장된 로그 확인 가능.
    ※ 깃 연동 하는 법
    ** git remote add origin https://github.com/sanheekim/project2022-languageOfAI.git
8. Django는 DB 종류와 상관없이 DB작업을 할 수 있는 프레임워크. (settings.py의 DATABASES 확인)
(가상환경 접속해서 cd myproject 한 상태)
py manage.py migrate 할 것.

### 사용기술 : Google Cloud Speech API
