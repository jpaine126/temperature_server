sudo docker run \
-d \
-v /var/www/temperature_server:/app/database \
-p 8000:8000 \
server \
