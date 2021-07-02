FROM nginx:latest
RUN apt-get update -y
# EXPOSE 80
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

