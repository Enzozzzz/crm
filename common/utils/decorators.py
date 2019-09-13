from functools import wraps
from flask import g, request


# 验证是否登录
from common.utils.rbac.get_menu import get_menu


def login_required(f):
    """
    用户必须登录装饰器
    使用方法：放在method_decorators中
    """
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not g.user_id:
            return {'message': 'User must be authorized.'}, 401
        return f(*args, **kwargs)
    return wrapper


# 验证菜单访问权限
# 验证是否登录
def menu_permission_required(f):
    """
    访问菜单时,必须有访问权限
    使用方法：放在method_decorators中
    """
    @wraps(f)
    def wrapper(*args, **kwargs):

        # return request.url
        url = request.url
        hosts = "http://127.0.0.1:5000"
        url = url.replace(hosts, "")
        user_id = g.user_id
        url_list = get_menu(user_id)
        for url_dict in url_list:
            if url == url_dict["url"]:
                return f(*args, **kwargs)
        else:
            return {"message": "you have no url Permission !"}, 400


    return wrapper