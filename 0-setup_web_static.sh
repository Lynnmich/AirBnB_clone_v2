#!/usr/bin/env bash
# Script that sets up a web server for deployment of web_static.

# Update and Install Nginx
sudo apt-get update
sudo apt-get install -y nginx

# Create folders if they don't exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file for testing
echo "Hello World!" | sudo tee /data/web_static/releases/test/index.html

# Create or recreate symbolic link
sudo rm -rf /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data/ folder to ubuntu user and group
sudo chown -hR ubuntu:ubuntu /data/

# Update Nginx configuration
CONFIG_FILE="/etc/nginx/sites-available/default"
CONFIG_BLOCK="location /hbnb_static {\n\talias /data/web_static/current/;\n}\n"
sudo sed -i "/server_name _;/a $CONFIG_BLOCK" $CONFIG_FILE

# Restart Nginx
sudo service nginx restart

exit 0
