from flask_login import logout_user
from app.models.User import token_required


class UserController:
    def __init__(self):
        pass

    @token_required
    def authorize_check():
        return {'status': True, "authorized": True}

    @token_required
    def logout():
        logout_user()
        return {'status': True, "logged_out": True}
