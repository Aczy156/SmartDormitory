# -*- coding: UTF-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def init_ext(app):
    db.init_app(app=app)
    migrate.init_app(app, db)
