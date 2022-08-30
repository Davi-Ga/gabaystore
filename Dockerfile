FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app /app

RUN python /app/manage.py collectstatic --noinput

RUN python /app/manage.py makemigrations && python /app/manage.py migrate

CMD gunicorn app.wsgi:application -b 0.0.0.0:8080