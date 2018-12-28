# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from great.models import User


class RegistrationForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    email = StringField('邮箱', validators=[DataRequired(), Email(message='请输入正确的邮箱格式')])
    password = PasswordField('密码', validators=[DataRequired()])
    password2 = PasswordField('验证密码', validators=[DataRequired(), EqualTo(fieldname='password', message='请输入相同的密码')])
    submit = SubmitField('注册')

    # validate_on_submit时会自动调用validate_%s的方法
    def validate_username(self, username):
        user = User.query.filter_by(name=username.data).first()
        if user is not None:
            raise ValidationError('用户名已存在')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('邮箱已被注册')


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired('请输入用户名')])
    password = PasswordField('密码', validators=[DataRequired('请输入密码')])
    submit = SubmitField('登录')
