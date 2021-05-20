FROM python:3.9.4
EXPOSE 80
RUN apt-get update -y && \
    apt-get autoremove --purge -y && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /eapi
ADD ./app ./app
ADD ./requirements.txt .
ADD ./data ./data
ADD ./alembic ./alembic
ADD ./alembic.ini ./alembic.ini
ADD ./tests ./tests
ADD ./commands.py .
ADD ./cmds ./cmds
ADD ./pytest.ini ./pytest.ini
ADD .env .env
RUN pip install -r requirements.txt
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
