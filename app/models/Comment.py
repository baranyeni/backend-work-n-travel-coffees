from app.models import db


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    user_id = db.Column(db.Integer,  nullable=False)
    shop_id = db.Column(db.Integer,  nullable=False)
    text = db.Column(db.String(255),  nullable=False)

    def __repr__(self):
        return '<Comments %r>' % self.text
