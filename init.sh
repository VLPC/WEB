sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
cd /home/box/web && sudo gunicorn -b 0.0.0.0:8080 hello:application &
sudo ln -sf /home/box/web/etc/gunicorn-django.conf /etc/gunicorn.d/test
cd /home/box/web/ask && sudo gunicorn -b 0.0.0.0:8000 ask.wsgi:application &
