FROM python:latest
EXPOSE 5000
RUN apt-get update -y --fix-missing
WORKDIR /opt/server
RUN pip install pipenv
ADD requirements.txt .
RUN pip install -r requirements.txt

