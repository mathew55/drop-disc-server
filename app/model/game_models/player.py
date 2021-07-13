import jsons

class Player:

    """
        Class which holds the player details
    """
    def __init__(self, name, token):
        self.name = name
        self.token = token

    def __str__(self):
        return self.name

    def to_ser_obj(self):
        return jsons.dump(self)