from flask import jsonify

from common.models.crm import MenuPermission, Menu
from common.utils.rbac.get_permissions import get_permission
from common.utils.rbac.get_roles import get_all_roles


def get_menu(user_id):
    """
    此函数需要传值:user_id
    :return:
    """
    # user_id = 1

    # 获取用户对应的所有角色
    role_list = get_all_roles(user_id)
    print("role_list:", role_list)

    # 根据角色id,获取对应的权限列表
    permission_list = get_permission(role_list)
    print("permission_list:", permission_list)

    # 根据权限id,获得用户的菜单id 以及菜单的对象
    menus_id = []
    for permission in permission_list:
        menus = MenuPermission.query.filter_by(permission_id=permission).all()
        for menu in menus:
            menus_id.append(menu.menu_id)

    # 对重复的数据进行去重
    menus_id = set(menus_id)
    menus_id = list(menus_id)

    # 获取菜单详情
    menu_detail = []
    for menu_id in menus_id:
        menu1 = {}
        menu = Menu.query.filter_by(id=menu_id).first()
        menu1["menu_id"] = menu_id
        menu1["menu_name"] = menu.name
        menu1["menu_url"] = menu.url
        menu_detail.append(menu1)

    # return jsonify(menu_detail)
    return menu_detail
