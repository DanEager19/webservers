#!/bin/bash
apt-get install docker.io
docker build -t flask:server .
docker run -d -p 80:5000 --restart always flask:server