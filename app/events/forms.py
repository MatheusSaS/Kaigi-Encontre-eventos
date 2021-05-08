from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms.widgets import TextArea
from wtforms import Form,IntegerField, StringField, validators,DateTimeField,TimeField,DecimalField,TextAreaField
from datetime import datetime
import decimal

class Form_Events(Form):
    name = StringField('Nome',[validators.DataRequired()])
    description = StringField('Descrição',[validators.DataRequired()], widget=TextArea())
    donation = StringField('Roupas',[validators.DataRequired()])
    local_name = StringField('Local',[validators.DataRequired()])
    address = StringField('Endereço ',[validators.DataRequired()])
    Street = StringField('Endereço ',[validators.DataRequired()])
    zipcode = StringField('CEP',[validators.DataRequired()])
    number = StringField('Número')
    complement = StringField('Complemento')
    district = StringField('Bairro')
    city = StringField('Cidade',[validators.DataRequired()])
    state = StringField('Estado',[validators.DataRequired()])
    
    start_date = DateTimeField('Data de Início',validators=[validators.InputRequired()],format = "%d/%m/%Y",default= datetime.now)
    start_time = TimeField('Hora de Término',validators=[validators.InputRequired()],format = "%H:%M",default= datetime.now)
    
    end_date = DateTimeField('Data de Término',validators=[validators.InputRequired()],format = "%d/%m/%Y",default= datetime.now)
    end_time = TimeField('Hora de Término',validators=[validators.InputRequired()],format = "%H:%M",default= datetime.now)
    
    image_1 = FileField('Image_1',validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'])])
    image_2 = FileField('Image_2',validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'])])
    image_3 = FileField('Image_3',validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'])])

class Form_Ticket(Form):
    name = StringField('Nome',[validators.DataRequired()])
    amount = IntegerField('Quantidade',[validators.DataRequired()])
    price = DecimalField('Preço',[validators.DataRequired()],default=0)
    
    start_date_sale = DateTimeField('Data de Início das vendas',validators=[validators.InputRequired()],format = "%d/%m/%Y",default= datetime.utcnow)
    start_time_sale = TimeField('Hora de Início',validators=[validators.InputRequired()],format = "%H:%M",default= datetime.utcnow)
    
    end_date_sale = DateTimeField('Data de Término das Vendas',validators=[validators.InputRequired()],format = "%d/%m/%Y",default= datetime.utcnow)
    end_time_sale = TimeField('Hora de Término',validators=[validators.InputRequired()],format = "%H:%M",default= datetime.utcnow)
    
    min_quantity = IntegerField('Quantidade',[validators.DataRequired()])
    max_quantity = IntegerField('Quantidade',[validators.DataRequired()])
    
    description = TextAreaField('Descrição')
    
    
    
    