from flask import request
from flask_restful import Resource

from common.models.crm import User, Role, UserRole, UserGroup, Group
from common.utils.decorators import login_required


class UserRolesPermission(Resource):
    """
    获取用户id,姓名,角色,用户组
    """
    method_decorators = [login_required]

    def get(self):
        users = User.query.all()

        role_list = []
        # 获取对应的列表
        for user in users:

            # 获取用户对应的角色
            userrole_list = []
            usergroup_list = []
            user_dict = {}
            user_dict['user_id'] = user.id

            # 获取用户角色id
            userroles = UserRole.query.filter_by(user_id=user.id).all()
            for userrole in userroles:
                role = Role.query.filter_by(id=userrole.id).first()
                userrole_list.append(role.name)
            user_dict['role'] = userrole_list

            # 获取用户的用户组
            usergroups = UserGroup.query.filter_by(user_id=user.id).all()
            for usergroup in usergroups:
                group = Group.query.filter(id=usergroup.id).first()
                usergroup_list.append(group.name)
            user_dict['group'] = usergroup_list

            # TODO 找到用户所在的角色在的用户组,也添加进去

            role_list.append(user_dict)

        return role_list
