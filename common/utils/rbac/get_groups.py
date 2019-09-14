from common.models.crm import Group, UserGroup


def get_user_group(user_id):
    """
    获取单个用户的用户组
    :param user_id:
    :return:
    """
    user_groups = UserGroup.query.filter_by(user_id=user_id).all()
    group_list = []
    for user_group in user_groups:
        group_detail = {}
        group = Group.query.filter_by(id=user_group.group_id).first()
        group_detail["group_id"] = group.id
        group_detail["name"] = group.name

        group_list.append(group_detail)

    return group_list


