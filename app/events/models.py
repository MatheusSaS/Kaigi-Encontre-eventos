from app import db
from datetime import datetime


class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), nullable=False,default='ATIVO')
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    local_name = db.Column(db.String(100), unique=False)  
    address = db.Column(db.String(100), unique=False) 
    zipcode = db.Column(db.String(50), unique=False) 
    Street = db.Column(db.String(100), unique=False) 
    number = db.Column(db.Integer,unique=False)
    complement = db.Column(db.String(50), unique=False) 
    district = db.Column(db.String(100), unique=False)     
    city = db.Column(db.String(50), unique=False)   
    state = db.Column(db.String(50), unique=False)   
    
    start_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  
    start_time = db.Column(db.Time, nullable=False, default=datetime.utcnow)  
    
    end_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  
    end_time = db.Column(db.Time, nullable=False, default=datetime.utcnow)  
          
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False)
    category = db.relationship('Category',backref=db.backref('posts', lazy=True))
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    user = db.relationship('User',backref=db.backref('posts', lazy=True))
    
    platforms_id = db.Column(db.Integer, db.ForeignKey('plataforms.id'),nullable=False)
    platforms = db.relationship('Plataforms',backref=db.backref('posts', lazy=True))
    
    ticket_id = db.Column(db.String, db.ForeignKey('ticket.id'),nullable=False)
    ticket = db.relationship('Ticket',backref=db.backref('posts', lazy=True))
    
    image_1 = db.Column(db.String(150), nullable=False,default='image.jpg')
    image_2 = db.Column(db.String(150), nullable=False,default='image.jpg')
    image_3 = db.Column(db.String(150), nullable=False,default='image.jpg')


    def __repr__(self):
        return '<Post %r>' % self.title

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(150), nullable=False,default='image.jpg')

class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Donation %r>' % self.name
    
class Plataforms(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    
    def __repr__(self):
        return '<Platforms %r>' % self.title
    
class Ticket(db.Model):
    __tablename__ = 'ticket'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45),nullable=False)
    amount = db.Column(db.Integer,unique=False)
    price = db.Column(db.Numeric(10,2), nullable=False,default=0)
    sold = db.Column(db.Integer, nullable=False)
    rate = db.Column(db.Numeric(10,2), nullable=False)
    type = db.Column(db.String(20),nullable=False)
    total = db.Column(db.Numeric(10,2), nullable=False)
    
    donation_id = db.Column(db.Integer,unique=False,default=0)   
    
    start_date_sale = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  
    start_time_sale = db.Column(db.Time, nullable=False, default=datetime.utcnow)  
    
    end_date_sale = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  
    end_time_sale = db.Column(db.Time, nullable=False, default=datetime.utcnow)  
    
    min_quantity = db.Column(db.Integer,unique=False)
    max_quantity = db.Column(db.Integer,unique=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    user = db.relationship('User',backref=db.backref('ticket_user', lazy=True))
    
    description = db.Column(db.String(200), nullable=False)
    
    def __repr__(self):
        return '<Ticket: {}>'.format(self.id)

db.create_all()