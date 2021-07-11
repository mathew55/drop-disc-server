from app.controller import app
from app.context.app_context import ApplicationContext


def startup(app):
    ApplicationContext.getContext()


if __name__ == '__main__':
    app.run()
    startup(app)
