from flask import Blueprint
from flask_restful import Api


crm_bp = Blueprint("crm", __name__)
crm_api = Api(crm_bp)

from resource.crm.passport import Login
crm_api.add_resource(Login, '/login')

