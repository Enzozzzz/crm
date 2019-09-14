from flask import Blueprint
from flask_restful import Api

from resource.crm.menu_access_test import Sales, SalesDirector, SalesManage, Cfo

crm_bp = Blueprint("crm", __name__)
crm_api = Api(crm_bp)


from resource.crm.menu_list import ShowMenu
from resource.crm.passport import Login, Menu
from resource.crm.admin import UserRolesPermission

crm_api.add_resource(Login, '/login')
crm_api.add_resource(Menu, '/menu')
crm_api.add_resource(UserRolesPermission, '/roles')
crm_api.add_resource(ShowMenu, '/show_menus')

# Test access Api
crm_api.add_resource(Sales, '/sales')
crm_api.add_resource(SalesDirector, '/sales_director_menu1')
crm_api.add_resource(SalesManage, '/show_menus')
crm_api.add_resource(Cfo, '/cfo_menu')

