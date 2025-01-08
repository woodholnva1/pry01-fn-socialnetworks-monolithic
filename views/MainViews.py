from flask import Blueprint, request

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
        self.blueprint.add_url_rule('/api/verifyMail', 'verifyMail', self.verifyMail, methods=["GET"])


    # Main Page
    def index(self):
        return self.servicesMain.index()

    def verifyMail(self):
        return self.servicesMain.verifyMail(request.args.get('mail'))


MainView(main_bp)
