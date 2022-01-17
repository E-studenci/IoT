FROM ubuntu:latest

WORKDIR /root

COPY / /root/rest

RUN apt update
RUN apt install -y python3-venv
RUN python3 -m venv .venv
RUN . /root/.venv/bin/activate && pip install -r /root/rest/requirements.txt

ENV FLASK_APP main.py
ENV FLASK_ENV development
ENV PYTHONPATH /root/rest/src/

CMD ["/root/.venv/bin/python3", "-m", "flask", "run", "-h", "0.0.0.0", "--no-debugger", "--no-reload"]