# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from great.models import User


class RegistrationForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired('请输入用户名')])
    email = StringField('邮箱', validators=[DataRequired('请输入邮箱地址'), Email('请输入正确的邮箱格式')])
    password = PasswordField('密码', validators=[DataRequired('请输入密码')])
    password2 = PasswordField('验证密码', validators=[
        DataRequired('请再次输入密码'),
        EqualTo(fieldname='password', message='请输入相同的密码')
    ])
    submit = SubmitField('注册')

    def validte_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
