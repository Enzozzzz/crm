from common.models import db


class User(db.Model):
    """
    用户表
    """
    __tablename__ = 'user'

    id = db.Column('id', db.Integer, primary_key=True, doc='用户id')
    name = db.Column(db.String, doc='姓名')
    password = db.Column(db.String, doc='密码')
    age = db.Column(db.String, doc='年纪')
