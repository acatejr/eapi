FROM python:latest
EXPOSE 5000
# RUN apt-get update -y --fix-missing
WORKDIR /opt/server
ADD requirements.txt .
RUN pip install -r requirements.txt
COPY $PWD/server/ .
# CMD ["bash"]
# CMD ["flask" "run" "-h" "0.0.0.0"]
