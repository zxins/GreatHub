# -*- coding: utf-8 -*-
import functools
from flask import (
    Blueprint, request, g, render_template, redirect, url_for, session
)

# url_prefix为关联的URL添加前缀
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    return render_template("register.html")
