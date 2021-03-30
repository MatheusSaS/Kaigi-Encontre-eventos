from app import db
from datetime import datetime


class Addorderhelp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), nullable=False,default='ATIVO')
    pub_date = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)
    type = db.Column(db.String(80), nullable=False,default='Pedido')
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False)
    category = db.relationship('Category',backref=db.backref('posts', lazy=True))
    
    image_1 = db.Column(db.String(150), nullable=False,default='image.jpg')
    image_2 = db.Column(db.String(150), nullable=False,default='image.jpg')
    image_3 = db.Column(db.String(150), nullable=False,default='image.jpg')


    def __repr__(self):
        return '<Post %r>' % self.title

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Category %r>' % self.name

db.create_all()