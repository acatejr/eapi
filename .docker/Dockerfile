FROM python:3.6.5
EXPOSE 8000
RUN apt-get update -y

WORKDIR /opt/app
CMD ['bash']
# COPY requirements.txt /opt/app
COPY . /opt/app/
RUN pip install -r requirements.txt

