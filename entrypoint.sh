#!/bin/sh
set -e

echo "Running migrations..."
python3 manage.py migrate
if [ $? -eq 0 ]; then
    echo "Migrations - OK"
else
    echo "Migrations failed"
    exit 1
fi

if [ "$DEBUG" = "False" ]
then
    python manage.py collectstatic --noinput
fi

if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL
fi

gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers=4

exec "$@"
