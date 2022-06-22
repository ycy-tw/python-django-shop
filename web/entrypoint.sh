#!/bin/sh
echo '# ------------------------------ #'
echo '#         Run migration          #'
echo '# ------------------------------ #'

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
uwsgi --ini uwsgi.ini

exec "$@"

