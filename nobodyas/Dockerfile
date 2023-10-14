FROM python:latest

WORKDIR /opt/nobodyas

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
ENV UWSGI_PROCESSES 1
ENV UWSGI_THREADS 16
ENV UWSGI_HARAKIRI 240
ENV DJANGO_SETTINGS_MODULE 'nobodyas.settings'

COPY requirements.txt requirements.txt
COPY /uwsgi/uwsgi.ini uwsgi.ini
COPY run_uwsgi.sh run_uwsgi.sh
COPY wait-for-it.sh wait-for-it.sh

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .

RUN chmod +x run_uwsgi.sh
RUN chmod +x wait-for-it.sh

ENTRYPOINT [ "./wait-for-it.sh", "database:5432", "--strict", "--timeout=300", "--", "./run_uwsgi.sh" ]