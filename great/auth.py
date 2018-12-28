# -*- coding: utf-8 -*-
import functools
from great.db import db_session
from great.models import User
from great.forms import RegistrationForm, LoginForm
from great import login_manager
from flask_login import login_user, current_user, logout_user
from werkzeug.urls import url_parse

from flask import (
    Blueprint, request, g, render_template, redirect, url_for, session, flash
)

# url_prefix为关联的URL添加前缀
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()

    # 这里会自动调用form中实现的validate_%s的函数
    if form.validate_on_submit():
        user = User(name=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db_session.add(user)
        db_session.commit()

        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('auth.login'))
    return render_template('register.html', title='Register', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    errors = []
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            errors.append('用户名或密码无效')
            return render_template("login.html", form=form, errors=errors)

        login_user(user)

        # 重定向到登录之前的页面
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

    return render_template("login.html", form=form)


@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
