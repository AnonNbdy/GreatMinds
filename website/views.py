from flask import Blueprint, render_template, request, url_for, redirect
from website import db
from website.models import JobListing, Tutor
from Tutors import *


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@views.route('/home')
def home_page():
    return render_template('login.html')


@views.route('/about')
def about_page():
    return render_template('about.html')


@views.route('/student', methods=['GET', 'POST'])
def student():
    return ''


@views.route('/index.html', methods=['GET', 'POST'])
def index():
    tutor = Tutor.query.all()
    return render_template('index.html', Tutor=tutor)


# @views.route('')

@views.route('application page.html', methods=['GET', 'POST'])
def appform():
    return render_template('application page.html')
