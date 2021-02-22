# 기술 블로그

내가 공부한 내용을 정리하기 위한 블로그

## Virtual Envirment

**virtualenv 설치**

    pip install virtualenv

**virtualenv 구성**

    virtualenv myvenv

**virtualenv 실행**

    myvenv\scripts\activate

## Django

**django 설치**

    pip install django

**django 프로젝트 생성**

    django-admin startproject [이름]

**데이터 모델 변경점 확인**

    python manage.py makemigrations

**데이터 모델 DB에 반영**

    python manage.py migrate

**django 개발 서버 실행**

    python manage.py runserver - django 기본 웹 주소 - http://127.0.0.1:8000/

**django admin 관리자 계정 생성**

    python manage.py createsuperuser

## 추가 커맨드

**이미지 모듈 설치**

    pip install Pillow

**폼 꾸미기 모듈 설치**

    pip install django-widget-tweaks

**설치된 모듈 확인**

    pip list

**모듈 설치**

    pip install -r <파일명>

**장고 어드민 계정 기억 안날 때**

    python manage.py shell

        >>> from django.contrib.auth.models import User

        >>> superuers = User.objects.filter(is_superuser=True)

        >>> supersuers
        => 아이디 나옴

**장고 어드민 계정 비밀번호 수정**

    python manage.py changepassword admin

## UWSGI 설정파일

**uwsgi 설정파일**

    # uwsgi - django 용 config 파일
    [uwsgi]
    base = /home/ubuntu/hongsWeb

    home = %(base)/venv
    # 가상환경 주소
    chdir = %(base)
    # 프로젝트 경로
    module = mywebsite.wsgi:application

    socket = /tmp/django.sock
    # 이름은 마음대로
    chmod-socket = 666
    # 누구나 수정할 수 있다

    # master프로세스를 띄울것인가
    # master프로세스는 부모프로세스와 비슷한 개념
    # 자식 프로세스가 죽거나 살릴 때 log를 띄울 수 있음
    master = true

    # 스레드 사용
    enable-threads = true

    # 프로세스 관리
    pidfile = /tmp/django.pid

    # uwsgi가 꺼질때 소켓이나 pid파일 등을 지움
    vaccum = true

    # log남기기
    logger = file:/tmp/uwsgi.log

**실행** : uwsgi -i /etc/uwsgi/sites/mywebsite.ini

# Nginx 설정파일

**nginx 설정**

/etc/nginx/sites-enabled에 default

**포트번호 수정**

**/etc/nginx/sites-enabled에 mywebsite로 하나 생성**

    upstream django {
        server unix:///tmp/django.sock;
    }
        server {
        listen 80;
        server_name localhost;
        charset utf-8;
        client_max_body_size 75M;
        location / {
            uwsgi_pass django;
            include /etc/nginx/uwsgi_params;
        }
    }

