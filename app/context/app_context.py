from app.connection_manager import Connections


class ApplicationContext:
    '''
        The applicationContext initialises and holds the playerPool and GameQueue to used across the application.
    '''

    __instance = None

    @staticmethod
    def getContext():
        """Static access method"""
        if ApplicationContext.__instance == None:
            print("Application Context not yet initialized, Initializing the Context")
            ApplicationContext()
        return ApplicationContext.__instance

    def __init__(self):
        if ApplicationContext.__instance != None:
            raise Exception("The Configurations are already loaded in memory, Please reuse the configs")
        else:
            player_pool = Connections()
            self.registerPlayerPool(player_pool)
            self.initializeGameQueue()
            ApplicationContext.__instance = self

    def registerPlayerPool(self, player_pool):
        self.player_pool = player_pool

    def initializeGameQueue(self):
        self.game_queue = []
        self.game_queue
