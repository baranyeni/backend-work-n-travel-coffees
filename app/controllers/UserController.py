from flask_login import login_required, logout_user


class UserController:
    def __init__(self):
        pass

    @login_required
    def authorize_check():
        return {'status': True, "authorized": True}

    @login_required
    def logout():
        logout_user()
        return {'status': True, "logged_out": True}
