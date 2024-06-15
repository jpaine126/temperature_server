FROM ubuntu:latest

# setup basics
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y python3-venv

RUN python3 --version

# copy stuff over
COPY ./requirements.txt ./

# sever reqs
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN python3 -m pip install -r ./requirements.txt

# cmd
COPY . /app/
# CMD


