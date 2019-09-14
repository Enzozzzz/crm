from flask_restful import Resource

from common.utils.decorators import menu_permission_required


class Sales(Resource):
    """
    Sales访问的接口
    """
    method_decorators = [menu_permission_required]
    def get(self):
        return "Sales, welcome to visit this page!"


class SalesDirector(Resource):
    """
    SalesDirector访问的接口
    """
    method_decorators = [menu_permission_required]

    def get(self):
        return "SalesDirector, welcome to visit this page!"


class SalesManage(Resource):
    """
    SalesManage访问接口
    """
    method_decorators = [menu_permission_required]

    def get(self):
        return "SalesManage, welcome to visit this page!"


class Cfo(Resource):
    """
    Cfo访问接口
    """
    method_decorators = [menu_permission_required]

    def get(self):
        return "CFO, welcome to visit this page!"





