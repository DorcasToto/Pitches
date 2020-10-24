
from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User
from .. import db
from flask_login import login_required,current_user
import datetime

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home '

    return render_template('index.html',title = title)