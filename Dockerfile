FROM python:3.8-buster as base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

FROM base as with-requirements

RUN pip3 install flake8

ARG BASE_DIR

WORKDIR ${BASE_DIR}

COPY requirements.txt ${BASE_DIR}

RUN pip3 install -r requirements.txt

