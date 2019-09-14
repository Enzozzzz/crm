
from common.models.crm import UserRole, Role, User


def get_son_roles(role_id, roles_list):
    """
    获取子角色
    :return:
    """
    print("role_id", role_id)
    if role_id is None:
        return roles_list

    print("role_id:", role_id)

    roles_list.append(role_id.id)

    roles_id = Role.query.filter_by(prole_id=role_id.id).all()
    #
    for role_id in roles_id:
        get_son_roles(role_id,roles_list)

    return roles_list


def get_all_roles(user_id):
    """
    获取当前用户的角色的子类角色id
    :param user_id:
    :return:
    """
    roles_list = []
    # 获取当前用户的角色集合
    userroles = UserRole.query.filter_by(user_id=user_id).all()
    print("roles:", userroles)

    # 对用户当前的角色遍历
    for userrole in userroles:
        print("role1:", userrole)

        # 将当前角色id添加到列表
        roles_list.append(userrole.role_id)

        # 获取当前角色的第一层子角色id
        roles_id = Role.query.filter_by(prole_id=userrole.role_id).all()
        for role_id in roles_id:
            get_son_roles(role_id, roles_list)

    return roles_list


def get_user_roles(user_id):
    """
    获取当前用户的角色id列表
    :param user_id:
    :return:
    [{"role_id":1,"role_name":"sales"},......]
    """
    role_list = []
    userroles = UserRole.query.filter_by(user_id=user_id).all()

    # 获取角色id,名称
    for userrole in userroles:

        role_detail = {}
        role = Role.query.filter_by(id=userrole.role_id).first()
        role_detail["role_id"] = role.id
        role_detail["name"] = role.name
        role_list.append(role_detail)

    return role_list







