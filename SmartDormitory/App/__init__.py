# -*- coding: UTF-8 -*-

from datetime import timedelta
from flask import Flask
from App.configurations.ext import init_ext
from App.configurations.settings import envs
from App.views.user import userBlue
from App.views.dormitory import dormitoryBlue
from App.views.log import logBlue


def create_app(env):
    app = Flask(__name__)
    app.config.from_object(envs.get(env))

    app.register_blueprint(userBlue)
    app.register_blueprint(dormitoryBlue)
    app.register_blueprint(logBlue)

    init_ext(app=app)

    app.config['SECRET_KEY'] = 'housebrain will change the world'
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
