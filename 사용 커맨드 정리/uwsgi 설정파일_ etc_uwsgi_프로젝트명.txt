uwsgi 설정파일

# uwsgi - django 용 config 파일
[uwsgi]
base = /home/ubuntu/hongsWeb

home = %(base)/venv # 가상환경 주소
chdir = %(base) # 프로젝트 경로
module = mywebsite.wsgi:application

socket = /tmp/django.sock # 이름은 마음대로
chmod-socket = 666 # 누구나 수정할 수 있다

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

실행 : uwsgi -i /etc/uwsgi/sites/mywebsite.ini