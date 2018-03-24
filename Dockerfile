FROM python:3.6.4
EXPOSE 5000

RUN apt-get update -y
RUN apt-get install -y mongodb-clients psmisc
WORKDIR /opt/app/
COPY . /opt/app/
RUN pip install -r requirements.txt
