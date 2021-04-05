from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_uploads import IMAGES, UploadSet, configure_uploads,patch_request_class
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///helpsdb.db'
app.config['SECRET_KEY'] = 'jwkhfciuewfwzf323f3'
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images/')
app.config['UPLOADED_PHOTOS_DEST_CONVERT'] = os.path.join(basedir, 'static/images_corverted/')

photos = UploadSet('photos',IMAGES)
configure_uploads(app,photos)
patch_request_class(app)

db = SQLAlchemy(app)
bycrypt = Bcrypt(app)

from app.admin import routes
from app.order_helps import routes