FROM ubuntu:20.04

RUN apt-get update && apt-get install -y nginx

COPY index.html /var/www/html/index.nginx-debian.html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]