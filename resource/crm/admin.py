from flask import request, jsonify
from flask_restful import Resource

from common.models.crm import User, Role, UserRole, UserGroup, Group
from common.utils.decorators import login_required, menu_permission_required
from common.utils.rbac.get_groups import get_user_group
from common.utils.rbac.get_roles import get_user_roles


class UserRolesPermission(Resource):
    """
    获取用户id,姓名,角色,用户组
    """
    method_decorators = [login_required]

    def get(self):

        users = User.query.filter().all()
        data = []
        for user in users:

            user_role_group = {}
            # 获取用户角色列表
            role_list = get_user_roles(user.id)

            # 获取用户组列表
            group_list = get_user_group(user.id)

            # 数据格式处理
            user_role_group["user_id"] = user.id
            user_role_group["role_list"] = role_list
            user_role_group["group_list"] = group_list

            data.append(user_role_group)

        return jsonify(data)
