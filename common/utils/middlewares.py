from flask import request, g

from .jwt_utils import verify_jwt


def jwt_authentication():
    """
    根据jwt验证用户身份
    """
    g.user_id = None
    g.url = None
    token = request.headers.get('Authorization')
    if token:
        payload = verify_jwt(token)
        if payload:
            g.user_id = payload.get('user_id')
            g.url = request.url


