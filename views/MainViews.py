from flask import Blueprint, current_app

from services.ServicesMain import ServicesMain

main_bp = Blueprint('main', __name__)

# Class Vista Index
class MainView:
    def __init__(self, blueprint):
        self.blueprint = blueprint
        self.register_routes()

        # Servicios
        self.servicesMain = ServicesMain()

    def register_routes(self):
        self.blueprint.add_url_rule('/', 'index', self.index)

    # Main Page
    def index(self):
        return self.servicesMain.index()


MainView(main_bp)
