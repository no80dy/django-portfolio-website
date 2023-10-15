#!/usr/bin/env bash

set -e

chown www-data:www-data /var/log
chown -R www-data:www-data /opt/nobodyas/media

python3 manage.py migrate
python3 manage.py collectstatic --no-input

uwsgi --strict --ini uwsgi/uwsgi.ini
