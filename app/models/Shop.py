from app.models import db


class Shop(db.Model):
    __tablename__ = 'shops'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    rating = db.Column(db.Integer)
    ratingCount = db.Column(db.Float)
    # city = TODO: add relation model with has_one relation
    address = db.Column(db.String(80), unique=True, nullable=False)
    imageUrl = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name
