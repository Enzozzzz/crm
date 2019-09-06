import jwt
from flask import current_app


def generate_jwt(payload, expiry, secret=None):
    """
    生成jwt
    :param payload: dict 载荷
    :param expiry: datetime 有效期
    :param secret: 密钥
    :return: jwt
    """
    _payload = {'exp': expiry}
    _payload.update(payload)

    if not secret:
        secret = current_app.config['JWT_SECRET']

    token = jwt.encode(_payload, secret, algorithm='HS256')
    return token.decode()


def verify_jwt(token, secret=None):
    """
    检验jwt
    :param token: jwt
    :param secret: 密钥
    :return: dict: payload
    """
    if not secret:
        secret = current_app.config['JWT_SECRET']

    try:
        payload = jwt.decode(token, secret, algorithm=['HS256'])
    except jwt.PyJWTError:
        payload = None

    return payload
