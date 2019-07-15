# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from flask_migrate import Migrate

db = SQLAlchemy()
redis_store = FlaskRedis()
migrate = Migrate()
