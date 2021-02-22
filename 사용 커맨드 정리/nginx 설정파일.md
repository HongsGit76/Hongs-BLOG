nginx 설정

/etc/nginx/sites-enabled에 default 

포트번호 수정




/etc/nginx/sites-enabled에 mywebsite로 하나 생성

upstream django {
    server unix:///tmp/django.sock;
}
                                                                                                                                          server {
    listen 80;
    server_name localhost;                                                                                                               charset utf-8;                                                                                                                           client_max_body_size 75M;                                                                                                             location / {
        uwsgi_pass django;                                                                                                                   include /etc/nginx/uwsgi_params;                                                                                            }
}

