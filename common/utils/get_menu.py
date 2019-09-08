from flask import g

from common.models.crm import UserRole, RolePermission, MenuPermission, Menu


def get_menu(user_id):

    menus_ids = []

    roles = UserRole.query.filter_by(user_id=user_id).all()
    print(roles)

    # 取出角色对应的权限
    for role in roles:
        permissions = RolePermission.query.filter_by(role_id=role.role_id).all()

        # 取出对应的菜单id
        for permission in permissions:
            menus = MenuPermission.query.filter_by(permission_id=permission.permission_id).all()
            for menu in menus:
                menus_ids.append(menu.menu_id)

    # 数据库中取出菜单对象
    menu_list = []

    for menus_id in menus_ids:
        menu_dict = {}
        menu = Menu.query.filter_by(id=menus_id).first()
        menu_dict["id"] = menu.id
        menu_dict["name"] = menu.name
        menu_dict["url"] = menu.url
        menu_list.append(menu_dict)

    return menu_list
