# -*- coding: utf-8 -*-
import functools
from great.db import db_session
from great.models import User
from great.forms import RegistrationForm, LoginForm
from flask_login import login_required, current_user

from flask import (
    Blueprint, request, g, render_template, redirect, url_for, session, flash
)

index_bp = Blueprint('index', __name__)


@index_bp.route('/')
@index_bp.route('/index')
def index():
    return render_template('index.html', title='Home Page')
