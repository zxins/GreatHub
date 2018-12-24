# -*- coding: utf-8 -*-
import functools
from great.db import db_session
from great.models import User
from great.forms import RegistrationForm

from flask import (
    Blueprint, request, g, render_template, redirect, url_for, session, flash
)

# url_prefix为关联的URL添加前缀
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        user = User.query.filter_by(name=form.username.data).first()
        if user is None:
            user = User(name=username, email=email)
            user.set_password(password)
            db_session.add(user)
            db_session.commit()
            return render_template('login.html')
        else:
            flash('User {} is already registered.'.format(username))
    return render_template("register.html", form=form)
