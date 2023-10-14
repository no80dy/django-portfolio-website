#!/usr/bin/env bash

set -e

python3 manage.py migrate
python3 manage.py collectstatic --no-input

chown www-data:www-data /var/log
chown -R www-data:www-data /opt/nobodyas/media

uwsgi --strict --ini uwsgi/uwsgi.ini
