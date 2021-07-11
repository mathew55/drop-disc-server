from flask import Flask

from app.controller.healthcheck_controller import health_check_ep
from app.controller.game_controller import game_controller

app = Flask(__name__)

app.register_blueprint(health_check_ep)
app.register_blueprint(game_controller)