# -*- coding: utf-8 -*-
import os
from flask import Flask


def create_app(test_config=None):
    from great.db import db_session
    from great import auth

    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(auth.auth_bp)

    # instance_relative_config=True 告诉应用配置文件是相对于 instance folder 的相对路径。
    # 实例文件夹在 flaskr 包的外面，用于存放本地数据（例如配置密钥和数据库），不应当 提交到版本控制系统。
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'great.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.mkdir(app.instance_path)
    except OSError:
        pass

    @app.teardown_appcontext
    def close_session(exception=None):
        db_session.remove()

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
