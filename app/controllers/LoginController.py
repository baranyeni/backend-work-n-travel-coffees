import flask
from flask import redirect, request, flash
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.User import User
from app import db


class LoginController:
    def __init__(self):
        pass

    def login():
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        next_url = request.form.get('next_url')

        user = User.query.filter_by(email=email).first()

        if user is None:
            return flask.render_template('app/login/login.html')
        elif User.check_password(user, password=password):
            login_user(user, remember=remember)

            if next_url is not None:
                return flask.redirect(next_url)
            else:
                return "Congrats! You are now logged in.."
        else:
            flash("Wrong password or something")
            return redirect('/login')

    def signup():
        if flask.request.method == 'GET':
            return flask.render_template('app/login/signup.html')

        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            flash("This user is already signed up! You can log in.")
            return redirect("/login")

        new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

        db.session.add(new_user)
        db.session.commit()

        return redirect("/admin")

    def logout():
        logout_user()
        return redirect("/")
