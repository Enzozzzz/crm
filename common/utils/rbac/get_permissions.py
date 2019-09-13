from common.models.crm import RolePermission


def get_permission(role_list):
    """
    根据角色id,获取权限id
    :return:
    """
    permission_list = []
    for role in role_list:
        rolepermissions = RolePermission.query.filter_by(role_id=role)
        for rolepermission in rolepermissions:
            permission_list.append(rolepermission.permission_id)

    return permission_list



