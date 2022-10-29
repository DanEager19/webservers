#!/bin/bash

sudo apt-get install -y python3 python3-pip python3-flask nginx

export FLASK_APP=app.py

apk add --no-cache gcc musl-dev linux-headers

pip install -r requirements.txt

sudo echo 'sudo /opt/mystery-form/run.sh &' >> /etc/profile

sudo cat >> /etc/nginx/sites-enabled/default << EOF
server {
    listen 80;
    location / {
      proxy_pass http://127.0.0.1:5000;
    }
}
EOF

sudo systemctl enable nginx && sudo systemctl start nginx