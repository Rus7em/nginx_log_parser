FROM python:3.12.5-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt


COPY . /app/

ENV PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=nginx_log_parser.settings

RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "nginx_log_parser.wsgi:application"]
