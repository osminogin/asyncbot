# asyncbot

Telegram messanger Bot with Celery task queue and Django (can be easily deployed to Heroku).

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```bash
git clone https://github.com/osminogin/asyncbot.git
cd asyncbot

pip install -r requirements.txt

# createdb asyncbotdb

python manage.py migrate
python manage.py collectstatic

heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```bash
heroku create
git push heroku master

heroku run python manage.py migrate
heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
- [Celery - Distributed Task Queue](http://docs.celeryproject.org/en/latest/)

## License

GPLv3
