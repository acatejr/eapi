FROM python:latest
EXPOSE 8000

RUN apt-get update -y
RUN apt-get install -y git build-essential libpq-dev python-dev sqlite3 libsqlite3-dev gcc postgis

WORKDIR /opt/app
COPY . /opt/app/
RUN pip install -r requirements.txt

# FROM ubuntu:16.04

# RUN apt-get update -y
# RUN apt-get install -y git build-essential libpq-dev python-dev sqlite3 libsqlite3-dev gcc python-pip

# RUN git clone git://github.com/yyuu/pyenv.git .pyenv
# RUN echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
# RUN echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
# RUN echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
# # RUN exec "$SHELL"
# RUN pyenv install 3.6.4
# RUN pyenv global 3.6.4
# # update pip
# # RUN python3.6 -m pip install pip --upgrade
# # RUN python3.6 -m pip install wheel

# # FROM python:3.6.5
# # EXPOSE 8000
# # RUN apt-get update -y
