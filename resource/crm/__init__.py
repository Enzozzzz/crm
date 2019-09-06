from flask import Blueprint
from flask_restful import Api


crm_bp = Blueprint("crm", __name__)
crm_api = Api(crm_bp)

from resource.crm.passport import Login, Menu
from resource.crm.admin import UserRolesPermission

crm_api.add_resource(Login, '/login')
crm_api.add_resource(Menu, '/menu')
crm_api.add_resource(UserRolesPermission, '/roles')

