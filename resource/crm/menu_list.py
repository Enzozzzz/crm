from flask import g
from flask_restful import Resource
from common.utils.decorators import login_required
from common.utils.rbac.get_menu import get_menu


class ShowMenu(Resource):
    """
    去数据库中取出对应的菜单list
    url:/show_menus
    """
    # method_decorators = [login_required]

    def get(self):

        menu_list = get_menu(g.user_id)
        return menu_list

