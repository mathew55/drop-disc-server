from app.controller import app
from app.context.app_context import ApplicationContext


def startup(app):
    ApplicationContext.getContext()

'''
    Responsible for collecting the controller endpoints and starting the app.
    Initializes the application context for the game server
'''
if __name__ == '__main__':
    app.run()
    startup(app)
