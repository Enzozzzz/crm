from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from common.models.crm import User


class Login(Resource):
    def get(self):
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
        # user = User.query.filter_by(username=username, password=password).first()
        # print(user1)

        # if user1 is None:
        user1 = User.query.filter().first()
        print(user1)
        return {"message": "login failed"}
