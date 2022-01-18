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

COPY /api-0.1-py3-none-any.whl /root/
COPY /tls /root/tls

RUN apt update
RUN apt install -y python3-venv
RUN python3 -m venv .venv
RUN /root/.venv/bin/pip install /root/api-0.1-py3-none-any.whl

CMD ["/root/.venv/bin/python3", "-m", "flask", "run", "-h", "0.0.0.0", "--no-debugger", "--no-reload"]