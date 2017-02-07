# -*- coding:utf-8 -*-
from flask import Flask
from flask.ext.login import LoginManager
import ConfigParser
import logging
import os

cf = ConfigParser.ConfigParser()
cf.read('b612.ini')

logger = logging.getLogger('webserver')
handler = logging.FileHandler(os.path.join(cf.get('webserver', 'log_path'), 'webserver.log'))
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('[%(levelname)s]\t%(asctime)s\t%(message)s'))
logger.addHandler(handler)

login_manager = LoginManager()
login_manager.session_protection = 'strong'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = cf.get('webserver', 'secret_key')
    login_manager.init_app(app)

    # 初始化蓝图
    from .main import admin
    app.register_blueprint(admin)

    return app
