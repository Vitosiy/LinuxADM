FROM ubuntu:20.10
RUN apt update && apt -y install nginx

RUN echo "daemon off;" >> /etc/nginx/nginx.conf

EXPOSE 80
EXPOSE 8080
EXPOSE 443

CMD [ "/usr/sbin/nginx" ]
