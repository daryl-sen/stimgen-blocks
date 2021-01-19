from flask import render_template, Blueprint, redirect, url_for, flash, request
from application.models import *

core = Blueprint('core', __name__, template_folder = 'templates/core')

@core.route('/')
def index():
    return render_template('index.html')

@core.route('/create', methods = ['GET', 'POST'])
def create():
    return render_template('template.html')

@core.route('/login')
def customize():
    return render_template('login.html')

@core.route('/register')
def register():
    return render_template('register.html')

@core.route('/license')
def license():
    return render_template('license.html')