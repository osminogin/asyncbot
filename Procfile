web: gunicorn asyncbot.wsgi --log-file -
worker: celery -A asyncbot worker -l info
