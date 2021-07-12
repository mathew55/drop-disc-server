from app.context.conf import Config
from app.model.response_models.response import Response

class HealthCheck(Response):

    def __init__(self):
        super(HealthCheck, self).__init__()
        self.config = Config()
        self.serviceName = self.config.get_config_value("thisService", "name")
        self.serviceVersion = self.config.get_config_value("thisService", "version")
        self.message = "Drop Disc Server is up, Let's keep playing"

    def to_json(self):
        return {
            "serviceName": self.serviceName,
            "serviceVersion": self.serviceVersion,
            "message": self.message
        }