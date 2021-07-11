from flask import Blueprint
from app.model.response_models.health_check_response import HealthCheck

health_check_ep = Blueprint('health_check_ep', __name__, template_folder="templates")

@health_check_ep.route('/ping', methods=['GET'])
def check_health():
    """Determins if the container is working and healthy. Returns a JSON object with relevant data regarding the health of the service"""
    health_check = HealthCheck()
    return health_check.response()
