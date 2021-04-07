from flask import render_template, session, request, redirect, url_for,flash,current_app
from wtforms import form
from app import app, db, photos
from app.admin.model import User
import secrets,os

@app.route('/vaquinha')
def vaquinha():
    return 'Vaquinha'