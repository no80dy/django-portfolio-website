FROM python:latest

WORKDIR /opt/nobodyas

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
ENV DJANGO_SETTINGS_MODULE 'nobodyas.settings'

COPY requirements.txt requirements.txt
COPY wait-for-it.sh wait-for-it.sh
COPY run_manage.sh run_manage.sh

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .

RUN chmod +x run_manage.sh
RUN chmod +x wait-for-it.sh

ENTRYPOINT [ "./wait-for-it.sh", "database:5432", "--strict", "--timeout=300", "--", "./run_manage.sh" ]