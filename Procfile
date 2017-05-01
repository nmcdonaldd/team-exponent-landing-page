heroku ps:scale web=1
web: gunicorn landing_page.app:application
heroku run source landing_page/bin/activate
heroku run python landing_page/landing_page.py
