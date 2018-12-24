# -*- coding: utf-8 -*-
from great.db import Base
from sqlalchemy import Column, Integer, String
from werkzeug.security import check_password_hash, generate_password_hash


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, index=True)
    email = Column(String(120), unique=True, index=True)
    password_hash = Column(String(128))

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)