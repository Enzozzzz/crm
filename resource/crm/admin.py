from flask_restful import Resource


class UserRolesPermission(Resource):
    """
    获取用户id,姓名,角色,用户组
    """
    def get(self):
        return "1111"
