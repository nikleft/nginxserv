sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo sudo /etc/init.d/nginx restart
gunicorn -c hello.py hello:application
curl -l http://127.0.0.1/hello/
