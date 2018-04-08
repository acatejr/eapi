FROM python:3.6.5
EXPOSE 8000
RUN apt-get update -y

WORKDIR /opt/app
COPY requirements.txt /opt/app
RUN pip install -r requirements.txt
