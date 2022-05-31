from flask_login import login_required


class UserController:
    def __init__(self):
        pass

    @login_required
    def authorize_check():
        return {'status': True, "authorized": True}
