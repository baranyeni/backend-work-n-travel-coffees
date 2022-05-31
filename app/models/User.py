from app.models import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(100))
    name = db.Column(db.String(80), unique=True, nullable=False)
    authenticated = db.Column(db.Boolean, default=False)
    admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<User %r>' % self.name

    def get(user_id):
        return User.query.filter_by(email=user_id).first()

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_admin(self):
        """Return admin column."""
        return self.admin

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False
<<<<<<< HEAD
=======
    def is_user_id(self):
        """Return , User Id Value"""
        return self.id
>>>>>>> 667a577 (relationship and endpoints addition)
