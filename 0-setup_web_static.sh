#!/usr/bin/env bash
# Script that sets up a web server for deployment of web_static.

#Update and Install Nginx
sudo apt-get update
sudo apt-get install -y nginx

#Create folders if they don't exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

#Create a fake html file
sudo echo "Hello World!" > /data/web_static/releases/test/index.html

#Create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#Give ownership of /data/ folder recursively
sudo chown -R ubuntu:ubuntu /data/

#Update Nginx config
sudo sed -i '/^\s*location \/hbnb_static/ {
    alias \/data\/web_static\/current\/;
}' /etc/nginx/sites-available/default

#Restart Nginx
sudo service nginx restart
