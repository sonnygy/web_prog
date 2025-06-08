FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ../requirements.txt /app/

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

EXPOSE 8001

CMD sh -c "daphne -b 0.0.0.0 -p $PORT django_project.asgi:application"
