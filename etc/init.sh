sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo sudo /etc/init.d/nginx restart
sudo /etc/init.d/gunicorn restart
#sudo gunicorn -c hello.py hello222:wsgiapp
sudo gunicorn -c djresp.py viewresp:test
