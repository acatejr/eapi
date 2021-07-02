FROM python:latest
RUN apt-get update -y
WORKDIR /usr/src/app
ADD requirements.txt .
RUN pip install pip --upgrade
RUN pip install -r requirements.txt
ADD . .

