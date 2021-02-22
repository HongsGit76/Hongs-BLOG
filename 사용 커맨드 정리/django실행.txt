# django 설치
    pip install django

# django 프로젝트 생성
    django-admin startproject [이름]

# django 앱 생성
    python manage.py startapp [이름]
    
    **기본세팅**
    
    생성된 앱 내의 클래스 이름 복사하여 settings.py의 INSTALLED_APPS에 추가
    세계시간 'UTC' -> 'Asia/Seoul' 로 변경
# url 규칙생성
    **필요 모듈 추가**
    
    [프로젝트명]/urls.py에
    
        from django.conf.urls import include
        from django.views.generic import RedirectView
        from django.conf import settings
        from django.conf.urls.static import static
        
    추가
    
    
    urlpatterns에 
    
        path('blog/', include('blog.urls')), # blog 라는 주소로 들어왔을 때 앱 내에서 처리
        path('',RedirectView.as_view(url='/blog/', permanent=True)), # 기본 주소로 들어왔을 때 블로그로 이동
        
    추가
    
     urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
     urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
     
    또한 추가
    
    생성한 앱의 폴더 안에 urls.py 생성
    
        from django.urls import path
        from blog import views
    
    추가

# 데이터 모델 변경점 확인
    python manage.py makemigrations

# 데이터 모델 DB에 반영
    python manage.py migrate

# django 개발 서버 실행
    python manage.py runserver
    - django 기본 웹 주소 - http://127.0.0.1:8000/
    
# 기본 url 주소 생성
    앱 내의 urls.py에 
    
        urlpatterns=[
            path("", views.index, name='index'),
        ]
        
    추가
    
    앱 내의 views.py에
    
    def index(req):
        context = {

        }

        return render(req, 'index.html', context=context)
        
    추가
    
    앱 내 templates라는 폴더 생성하여 index.html생성

# django admin 관리자 계정 생성
    python manage.py createsuperuser
