from flask import Flask
from flask_migrate import Migrate

from app.config import DevelopmentConfig
from app.models import db
from app.controllers import stadium_groups_controller
from app.controllers import stadiums_controller
from app.controllers import stadium_controller
from app.models.stadium_group import StadiumGroup
from app.models.stadium import Stadium
from app.models.address import Address
from app.models.user import User
from app.models.stadium_image import StadiumImage


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(DevelopmentConfig)

    app.register_blueprint(stadium_groups_controller.bp)
    app.register_blueprint(stadium_controller.bp)
    app.register_blueprint(stadiums_controller.bp)

    db.init_app(app)
    Migrate().init_app(app, db)

    return app
