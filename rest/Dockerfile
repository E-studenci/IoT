FROM ubuntu:latest

ENV FLASK_APP api
ENV FLASK_ENV development
ENV MONGO_HOST mongo
ENV REDIS_HOST redis
ENV REDIS_CRT redis.crt
ENV CLIENT_KEY client_2.key
ENV CLIENT_CRT client_2.crt
ENV KEY_FOLDER /root/tls

WORKDIR /root

COPY /api-0.1-py3-none-any.whl .
COPY /tls tls

RUN apt update &&\
    apt install -y python3-venv &&\
    python3 -m venv .venv &&\
    .venv/bin/pip install /root/api-0.1-py3-none-any.whl

CMD [".venv/bin/python3", "-m", "flask", "run", "-h", "0.0.0.0", "--no-debugger", "--no-reload"]