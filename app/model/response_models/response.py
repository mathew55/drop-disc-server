class Response:

    def __init__(self, payload= None, message="", code=None):
        self.payload = payload
        self.message = message
        self.code = code

    def build(self, payload=None, message="", code=None):
        self.payload = payload
        self.message = message
        self.code = code

    def to_json(self):
        if self.payload:
            return {
                "status": {
                    "message": self.message,
                    "code": self.code
                },
                "payload": self.payload
            }
        else:
            return {
                "status":{
                    "message": self.message,
                    "code": self.code
                }
            }

    def response(self):
        return self.to_json(), self.code

    def __repr__(self):
        return f"Response(" \
               f"payload={repr(self.payload)}, " \
               f"message={repr(self.message)}, " \
               f"status={repr(self.code)})"

    def __eq__(self, other):
        return self.payload == other.payload \
            and self.message == other.message \
            and self.code == other.code
