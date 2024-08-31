FROM python:3.12.5-slim

ARG FILE_FOR_PARSING
ENV FILE_FOR_PARSING=${FILE_FOR_PARSING}

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

ENV PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=nginx_log_parser.settings
