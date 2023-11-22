FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

RUN python manage.py makemigrations
RUN python manage.py migrate

CMD python manage.py runserver 0.0.0.0:8000