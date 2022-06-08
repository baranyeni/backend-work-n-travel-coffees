import flask
from flask import redirect, request, make_response, jsonify
from flask_login import logout_user
from werkzeug.security import generate_password_hash
from app.models.User import User
from app import db


class LoginController:
    def __init__(self):
        pass

    def login():
        post_data = request.form
        try:
            user = User.query.filter_by(
                email=post_data.get('email')
            ).first()
            auth_token = user.encode_auth_token(user.id)
            if auth_token:
                responseObject = {
                    'status': 'success',
                    'message': 'Successfully logged in.',
                    'auth_token': auth_token.decode()
                }
                return make_response(jsonify(responseObject)), 200
        except Exception as e:
            print(e)
            responseObject = {
                'status': 'fail',
                'message': 'Try again'
            }
            return make_response(jsonify(responseObject)), 500

    def signup():
        if flask.request.method == 'GET':
            return flask.render_template('app/login/signup.html')

        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            # flash("This user is already signed up! You can log in.")
            return redirect("/login")

        new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

        db.session.add(new_user)
        db.session.commit()

        try:
            user = User.query.filter_by(
                email=email
            ).first()

            auth_token = user.encode_auth_token(user.id)
            if auth_token:
                responseObject = {
                    'status': 'success',
                    'message': 'Successfully logged in.',
                    'auth_token': auth_token.decode()
                }
                return make_response(jsonify(responseObject)), 200
        except Exception as e:
            db.session.rollback()
            print(e)
            responseObject = {
                'status': 'fail',
                'message': 'Try again'
            }
            return make_response(jsonify(responseObject)), 500
        finally:
            db.session.close()

    def logout():
        logout_user()
        return redirect("/")
