from flask import render_template, session, request, redirect, url_for,flash
from wtforms import form
from app import app, db, bycrypt,photos
from .forms import RegistrationForm,LoginForm
from .model import User
import secrets
from app.events.models import Category, Donation, Plataforms

def CategoryList():
    category = Category.query.order_by(Category.id.desc()).all()
    return list(category)

def DonationList():
    donation = Donation.query.order_by(Donation.id.desc()).all()
    return list(donation)

def Plataformslist():
    donation = Plataforms.query.order_by(Plataforms.id.desc()).all()
    return list(donation)

@app.route('/admin')
def admin():
    if 'email' not in session:
        return redirect(url_for('login'))
    return render_template('admin/index.html',title='Admin Page')

@app.route('/category',methods=['GET'])
def category():
    category = CategoryList()    
    return render_template('admin/category.html',category=category)

@app.route('/addCategory', methods=['POST'])
def addCategory():        
       
    add_category = Category(name=request.form.get('category'))       
    db.session.add(add_category)
    flash('categoria adicionada')
    db.session.commit()
    return redirect(url_for('category'))

@app.route('/alterCategory/<int:id>',methods=['GET','POST'])
def alterCategory(id):
    alter_category = Category.query.get_or_404(id)
    category = request.form.get('category')
    if request.method == 'POST':
        alter_category.name = category
        flash('Categoria alterada')
        db.session.commit()
        return redirect(url_for('category'))
    return redirect(url_for('category'))

@app.route('/deletCategory/<int:id>',methods=['POST'])
def deletCategory(id):
    delete__category = Category.query.get_or_404(id)
    if request.method == "POST":
        db.session.delete(delete__category)
        db.session.commit()
        flash('Categoria deletada')
        return redirect(url_for('category'))
    return redirect(url_for('category'))

@app.route('/donation',methods=['GET'])
def donation():
    donations = DonationList()    
    return render_template('admin/donation.html',donations=donations)

@app.route('/addDonation', methods=['POST'])
def addDonation():    
    add_donation = Donation(name=request.form.get('donation'))       
    db.session.add(add_donation)
    flash('Doação adicionada')
    db.session.commit()
    return redirect(url_for('donation'))

@app.route('/alterDonation/<int:id>',methods=['GET','POST'])
def alterDonation(id):
    alter_donation = Donation.query.get_or_404(id)
    donation = request.form.get('donation')
    if request.method == 'POST':
        alter_donation.name = donation
        flash('Donation alterada')
        db.session.commit()
        return redirect(url_for('donation'))
    return redirect(url_for('donation'))

@app.route('/deletDonation/<int:id>',methods=['POST'])
def deletDonation(id):
    delete_donation= Donation.query.get_or_404(id)
    if request.method == "POST":
        db.session.delete(delete_donation)
        db.session.commit()
        flash('Donation deletada')
        return redirect(url_for('donation'))
    return redirect(url_for('donation'))


@app.route('/plataforms',methods=['GET'])
def plataforms():
    plataforms = Plataformslist()    
    return render_template('admin/plataforms.html',plataforms=plataforms)   
       
@app.route('/addPlataforms', methods=['POST'])
def addPlataforms():    
    add_donation = Plataforms(name=request.form.get('plataforms'))       
    db.session.add(add_donation)
    flash('Plataforma adicionada')
    db.session.commit()
    return redirect(url_for('plataforms'))

@app.route('/alterPlataforms/<int:id>',methods=['GET','POST'])
def alterPlataforms(id):
    alter_plataforma = Plataforms.query.get_or_404(id)
    plataforma = request.form.get('plataforms')
    if request.method == 'POST':
        alter_plataforma.name = plataforma
        flash('Plataforma alterada')
        db.session.commit()
        return redirect(url_for('plataforms'))
    return redirect(url_for('plataforms'))
       
@app.route('/deletPlataforms/<int:id>',methods=['POST'])
def deletPlataforms(id):
    delete_plataforma = Plataforms.query.get_or_404(id)
    if request.method == "POST":
        db.session.delete(delete_plataforma)
        db.session.commit()
        flash('Plataforma deletada')
        return redirect(url_for('plataforms'))
    return redirect(url_for('plataforms'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    flash('Obrigado por se registrar!')
    if request.method == 'POST' and form.validate():
        hash_password = bycrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data,email=form.email.data,password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash('Obrigado por se registrar!')
        return redirect(url_for('admin'))
    return render_template('admin/register.html', form=form,title="Registrar")

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bycrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            session['id'] = user.id
            session['name'] = user.name
            flash('Login efetuado corretamente')
            return redirect(request.args.get('next'))
        else:
            flash('Senha incorreto, tente novamente','danger')
        
    return render_template('admin/login.html',form=form,title="Login")

@app.route('/forgotPassword')
def forgotPassword():
    return render_template('admin/forgotPassword.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))