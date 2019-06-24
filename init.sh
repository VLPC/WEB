sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
gunicorn -с /etc/gunicorn.d/hello.py hello:application
sudo /etc/init.d/gunicorn restart﻿﻿

