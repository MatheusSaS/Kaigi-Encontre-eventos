from operator import add
from flask import render_template, session, request, redirect, url_for,flash,current_app
from wtforms import form
from app import app, db, photos
from .models import Addorderhelp, Category
from .forms import Addorderhelps
import secrets,os

def CategoryList():
    category = Category.query.order_by(Category.id.desc()).all()
    return list(category)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index',methods=['POST','GET'])
def index():
    if 'email' not in session:
        return redirect(url_for('login'))
    
    form = Addorderhelps(request.form)
    category = CategoryList()
    helps = Addorderhelp.query.all()
    return render_template('order_helps/index.html',title='Index',form=form,category=category,helps=helps)

@app.route('/addhelps',methods=['GET','POST'])
def addHelps():
    form = Addorderhelps(request.form)
    category = CategoryList()
    if request.method == 'POST':                     
        name = form.name.data
        description = form.description.data
        type = request.form.get('type')
        category = request.form.get('category')
        image = photos.save(request.files.get('image_1'),name=secrets.token_hex(10)+ ".")   
        
        addHelps = Addorderhelp(name=name,description=description,type=type,category_id=category,image_1=image)
        db.session.add(addHelps)
        flash('Pedido adicionado corretamente')
        db.session.commit()        
        return redirect(url_for('index'))
    return redirect(url_for('index'))

@app.route('/alterehelps/<int:id>',methods=['POST'])
def alterehelps(id):
    if request.method == 'POST':
        form = Addorderhelps(request.form)
        alterhelp = Addorderhelp.query.get_or_404(id)
        
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
