import datetime
from app.admin.routes import donation
from operator import add
from flask import render_template, session, request, redirect, url_for,flash,current_app,jsonify
from wtforms import form
from app import app, db, photos
from .models import Events, Category,Ticket,Donation,Plataforms
from .forms import Form_Events, Form_Ticket
from app.admin.model import User
from PIL import Image
import secrets,os
from datetime import date

def CategoryList():
    category = Category.query.order_by(Category.id.desc()).all()
    return list(category)

def resize(root,new_root,file):
    new_width = 600
    new_heigth = 400
    
    path = os.path.join(root,file)
    new_img_path = os.path.join(new_root,file)
    
    pillow_img = Image.open(path)
    new_img = pillow_img.resize((new_width,new_heigth), Image.LANCZOS)
    new_img.save(new_img_path)
        
@app.route('/')
def home():
    events = Events.query.all()
    category = Category.query.all()
    return render_template('events/home.html',events=events,category=category)

@app.route('/event/<int:id>')
def event(id): 
    events = Events.query.first_or_404()  
    id_ticket = events.ticket_id
    
    print(id_ticket) 
    ticket = Ticket.query.all()
    print(ticket)
    
    cidade = events.city
    estado = events.state
    nome = events.name
    start_date = events.start_date
    end_date = events.end_date
    return render_template('events/event.html',events=events,ticket=ticket,cidade=cidade,estado=estado,nome=nome,start_date=start_date,end_date=end_date)

@app.route('/list_events/<int:id>',methods=['GET'])
def list_events(id):
    events = Events.query.all()    
    return render_template('events/list_events.html',events=events)

@app.route('/json_list')
def json_list():
    events = Events.query.all()
    eventsList = []
    
    for event in events:
        eventsList.append({
            "id": event.id,
            "name": event.name,
            "image": event.image_1,
            "description":event.description,
        })
        
    return jsonify(eventsList=eventsList)

@app.route('/myEvents')
def myEvents():
    if 'email' not in session:
        return redirect(url_for('login'))
    events = Events.query.filter_by(user_id=session['id']).all()
    return render_template('events/my_events.html',events=events) 

@app.route('/create_event',methods=['POST','GET'])
def create_event(): 
    if 'email' not in session:
        return redirect(url_for('login'))
    form_events = Form_Events(request.form)
    form_ticket = Form_Ticket(request.form)
    category = Category.query.all()
    donation = Donation.query.all()
    ticket = Ticket.query.filter_by(user_id=session['id'])
    plataforms = Plataforms.query.all()               
                 
    return render_template('events/create_event.html',form=form_events,form_ticket=form_ticket,ticket=ticket,category=category,donation=donation,plataforms=plataforms)

@app.route('/post_event/<id>',methods=['POST'])
def post_event(id):
    if request.method == 'POST':
        form_events = Form_Events(request.form)
        image = photos.save(request.files.get('image_1'),name=secrets.token_hex(10)+ ".")         
        resize(app.config['UPLOADED_PHOTOS_DEST'],app.config['UPLOADED_PHOTOS_DEST_CONVERT'],image) 
                    
        day,month,year = request.form.get('start_date').split('/')         
        start_date = datetime.datetime(int(year),int(month),int(day))
        
        hour,minutes = request.form.get('start_time').split(':')      
        start_time = datetime.time(int(hour),int(minutes)) 
        
        year,month,year = request.form.get('end_date').split('/') 
        end_date = datetime.datetime(int(year),int(month),int(day)) 
        
        hour,minutes = request.form.get('end_time').split(':')   
        end_time = datetime.time(int(hour),int(minutes)) 
        
        add_event = Events(name=form_events.name.data,description=form_events.description.data,status='ATIVO',local_name=form_events.local_name.data,address=form_events.address.data,zipcode=form_events.zipcode.data,
                            Street=form_events.Street.data,number=form_events.number.data,complement=form_events.complement.data,district=form_events.district.data,city=form_events.city.data,state=form_events.state.data,
                            start_date=start_date,start_time=start_time,end_date=end_date,end_time=end_time,category_id=request.form.get('categoria'),ticket_id=id,
                            user_id=session['id'],platforms_id=request.form.get('plataforma'),image_1=image)         
        db.session.add(add_event)
        db.session.commit()     
        flash('Evento adicionado corretamente!')
        return redirect(url_for('home')) 

@app.route('/create_ticket',methods=['POST'])
def create_ticket():
    form_ticket = Form_Ticket(request.form)
    if request.method == 'POST':
        rate = 2
        total = rate + form_ticket.price.data
        add_ticket = Ticket(name=form_ticket.name.data,amount=form_ticket.amount.data,price=form_ticket.price.data,start_date_sale=form_ticket.start_date_sale.data,
                        start_time_sale=form_ticket.start_time_sale.data,end_date_sale=form_ticket.end_date_sale.data,end_time_sale=form_ticket.end_time_sale.data,
                        min_quantity=form_ticket.min_quantity.data, max_quantity=form_ticket.max_quantity.data, description=form_ticket.description.data,sold=0,rate=rate,
                        type=request.form.get('type').title(),donation_id=request.form.get('donation'),total=total,user_id=session['id'])
        db.session.add(add_ticket)
        db.session.commit()
        flash('Ingresso cadastrado!')
        return jsonify(data={'message': 'hello {}'.format(form_ticket.name.data)})
    return jsonify(data=form_ticket.errors)

@app.route('/alterTicket/<int:id>',methods=['POST'])
def alterTicket(id):
    form_ticket = Form_Ticket(request.form)
    if request.method == 'POST':        
        ticket = Ticket.query.get_or_404(id)        
        donation = request.form.get('donation')
        type = request.form.get('type')
        
        ticket.name = form_ticket.name.data
        ticket.amount = form_ticket.amount.data
        ticket.price = form_ticket.price.data
        ticket.type = type.title()
        ticket.donation_id = donation
        
        day,month,year = request.form.get('start_date_sale').split('/')         
        ticket.start_date_sale = datetime.datetime(int(year),int(month),int(day))
        
        hour,minutes,sec = request.form.get('start_time_sale').split(':')      
        ticket.start_time_sale = datetime.time(int(hour),int(minutes)) 
        
        year,month,year = request.form.get('end_date_sale').split('/') 
        ticket.end_date_sale = datetime.datetime(int(year),int(month),int(day)) 
        
        hour,minutes,sec = request.form.get('end_time_sale').split(':')   
        ticket.end_time_sale = datetime.time(int(hour),int(minutes)) 
        
        ticket.min_quantity = form_ticket.min_quantity.data
        ticket.max_quantity = form_ticket.max_quantity.data
        
        ticket.description = form_ticket.description.data
        
        db.session.commit()
        flash('Ingresso alterada corretamente')            
        return jsonify(data={'message': 'hello {}'.format(form_ticket.name.data)})
    return jsonify(data=form_ticket.errors)

@app.route('/deletTicket/<int:id>',methods=['POST'])
def deletTicket(id):    
    if request.method == "POST":
        ticket = Ticket.query.get_or_404(id)
        db.session.delete(ticket)
        db.session.commit()
        flash('Categoria deletada')
        return jsonify(data={'message': 'hello {}'.format(ticket.name)})
    return jsonify(data='Error')

@app.route('/contact')
def contact():
    return render_template('order_helps/contact.html')

@app.route('/about')
def about():
    return render_template('order_helps/about-company.html')



# *retirar

@app.route('/addhelps',methods=['GET','POST'])
def addHelps():
    form = Form_Events(request.form)
    category = CategoryList()    
    
    if request.method == 'POST':                                   
        name = form.name.data
        description = form.description.data
        type = request.form.get('type')
        category = request.form.get('category')
        image = photos.save(request.files.get('image_1'),name=secrets.token_hex(10)+ ".")         
        resize(app.config['UPLOADED_PHOTOS_DEST'],app.config['UPLOADED_PHOTOS_DEST_CONVERT'],image)        
            
        addHelps = Events(name=name,description=description,type=type,category_id=category,image_1=image,user_id=session['id'])
        db.session.add(addHelps)
        flash('Pedido adicionado corretamente')
        db.session.commit()        
        return redirect(url_for('home'))
    return redirect(url_for('home'))

@app.route('/alterehelps/<int:id>',methods=['POST'])
def alterehelps(id):
    if request.method == 'POST':
        form = Form_Events(request.form)
        alterhelp = Events.query.get_or_404(id)
        
        type = request.form.get('type')
        category = request.form.get('category')
        
        alterhelp.name = form.name.data
        alterhelp.description = form.description.data
        alterhelp.type = type
        alterhelp.category_id = int(category)
        try:
            os.unlink(os.path.join(current_app.root_path,"static/images/"+ alterhelp.image_1))
            alterhelp.image_1 = photos.save(request.files.get('image_1'),name=secrets.token_hex(10)+ ".")
        except:
            alterhelp.image_1 = photos.save(request.files.get('image_1'),name=secrets.token_hex(10)+ ".")
        db.session.commit()
        flash('Ajuda alterada corretamente')
            
        return redirect(url_for('addHelps'))
    return redirect(url_for('addHelps'))

@app.route('/deletehelp/<int:id>',methods=['POST'])
def deletehelp(id):
    if request.method == 'POST':
        deletehelp = Events.query.get_or_404(id)
        db.session.delete(deletehelp)
        db.session.commit()
        flash('Pedido excluido!')
        return redirect(url_for('home'))
    return redirect(url_for('indhomeex'))
