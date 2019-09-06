from datetime import datetime, timedelta
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from flask import current_app
from common.models.crm import User
from common.utils.jwt_utils import generate_jwt


class Login(Resource):

    def _generate_tokens(self, user_id, with_refresh_token=True):
        """
        生成token 和refresh_token
        :param user_id: 用户id
        :return: token
        """
    def get(self):
        print(current_app.config['SQLALCHEMY_DATABASE_URI'])
        return "get"

    def post(self):

        # 获取参数 进行校验
        json_parser = RequestParser()
        json_parser.add_argument('username', required=True)
        json_parser.add_argument('password', required=True)
        args = json_parser.parse_args()
        username = args.username
        password = args.password

        print(username, password)

        # 校验用户名 密码是否匹配 这里做粗略的校验
        user = User.query.filter_by(username=username, password=password).first()
        if user is None:
            return {"message": "login failed"}

        # 生成 jwt token 返回给前端
        user_id = user.id
        now = datetime.utcnow()
        expiry = now + timedelta(hours=2)
        token = generate_jwt({'user_id': user_id}, expiry)
        print("jwt token:", token)

        # 返回用户对应的url

        return token


class Menu(Resource):
    """
    返回菜单相关的数据给到前端
    return: menu_list
    """
    def get(self):
        return "list"