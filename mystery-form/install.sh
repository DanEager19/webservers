#!/bin/bash

apt-get install -y python3 python3-pip python3-flask nginx

mkdir /var/www/application
cp -r ./* /var/www/application 
chown -R www-data:www-data /var/www/application/

export FLASK_APP=/var/www/application/app.py

echo 'flask run --host=0.0.0.0 &' >> /etc/profile

cat >> /etc/nginx.conf << EOF
server {
    listen 80;
    server_name _;
    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-Host $host;
        proxy_set_header X-Forwarded-Prefix /;
    }
}
EOF

systemctl enable nginx && systemctl start nginx