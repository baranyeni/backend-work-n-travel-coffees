# This file was created to run the application on heroku using gunicorn.
# Read more about it here: https://devcenter.heroku.com/articles/python-gunicorn

from flask import render_template
from app import app


@app.route('/')
def index():
    return render_template("app/index/index.html")


if __name__ == '__main__':
    app.run()
