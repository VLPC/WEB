sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE db_stepic;"
mysql -uroot -e "CREATE USER 'box@localhost' IDENTIFIED BY 'pass123';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON db_stepic.* TO 'box@localhost' WITH GRANT OPTION;"
~/web/ask/manage.py makemigrations
~/web/ask/manage.py migrate
