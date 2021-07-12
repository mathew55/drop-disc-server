from flask import Blueprint
from app.model.response_models.health_check_response import HealthCheck
from app.context.conf import Config

health_check_ep = Blueprint('health_check_ep', __name__, template_folder="templates")
config = Config()
baseEndpoint = config.get_config_value("endpoint", "base")

@health_check_ep.route(f'{baseEndpoint}/ping', methods=['GET'])
def check_health():
    """Determins if the container is working and healthy. Returns a JSON object with relevant data regarding the health of the service"""
    health_check = HealthCheck()
    return health_check.response()
