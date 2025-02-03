FROM python:3
USER root

WORKDIR /app

RUN apt-get update
RUN apt-get install -y vim less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN python -m pip install jupyterlab
