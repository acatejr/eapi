FROM python:latest
EXPOSE 5000
RUN apt-get update -y
WORKDIR /opt/server
ADD requirements.txt .
RUN pip install -r requirements.txt
COPY $PWD/server/ .
