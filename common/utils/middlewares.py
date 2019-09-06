from flask import request, g

from .jwt_utils import verify_jwt


def jwt_authentication():
    """
    根据jwt验证用户身份
    """
    g.user_id = None
    authorization = request.headers.get('Authorization')
    print("authorization:", authorization)
    if authorization:
        payload = verify_jwt(authorization)
        if payload:
            g.user_id = payload.get('user_id')
        print("payload:", payload)
