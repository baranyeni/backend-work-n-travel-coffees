from app.models import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    authenticated = db.Column(db.Boolean, default=False)


def __repr__(self):
    return '<User %r>' % self.name


def is_active(self):
    """True, as all users are active."""
    return True


def get_id(self):
    """Return the email address to satisfy Flask-Login's requirements."""
    return self.email


def is_authenticated(self):
    """Return True if the user is authenticated."""
    return self.authenticated


def is_anonymous(self):
    """False, as anonymous users aren't supported."""
    return False
