# This file was created to run the application on heroku using gunicorn.
# Read more about it here: https://devcenter.heroku.com/articles/python-gunicorn

from flask import render_template, request
from app import app


@app.route('/')
def index():
    return render_template("app/index/index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    print(request)

    return render_template('app/login/login.html', form=request.form)


if __name__ == '__main__':
    app.run()
