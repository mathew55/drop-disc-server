from queue import Queue
import logging
import os

log = logging.getLogger("drop-disc-server")
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

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
            self.initializePlayerPool()
            self.initializeGameQueue()
            self.log = log
            ApplicationContext.__instance = self

    def initializePlayerPool(self):
        '''Initializes player pool'''
        self.player_pool = Queue(maxsize=2)

    def initializeGameQueue(self):
        self.game_queue_map = {}
