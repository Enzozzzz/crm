from common.models import db


class User(db.Model):
    """
    用户表
    """
    __tablename__ = 'user'

    id = db.Column('id', db.Integer, primary_key=True, doc='用户id')
    username = db.Column(db.String, doc='姓名')
    password = db.Column(db.String, doc='密码')
    age = db.Column(db.String, doc='年纪')


class Role(db.Model):
    """
    角色表
    """
    __tablename__ = 'role'
    id = db.Column('id', db.Integer, primary_key=True, doc='角色id')
    name = db.Column(db.String, doc='名称')
    prole_id = db.Column(db.Integer, doc='父类id')


class UserRole(db.Model):
    """
    用户角色表
    """
    __tablename__ = 'user_role'
    id = db.Column('id', db.Integer, primary_key=True, doc='id')
    user_id = db.Column(db.String, doc='用户id')
    role_id = db.Column(db.String, doc='角色id')


class Group(db.Model):
    """
    用户组表
    """
    __tablename__ = 'ugroup'
    id = db.Column('id', db.Integer, primary_key=True, doc='用户组id')
    name = db.Column(db.String, doc='名称')
    pgroup_id = db.Column(db.Integer, doc='用户组id')


class UserGroup(db.Model):
    """
    用户-组表
    """
    __tablename__ = 'user_group'
    id = db.Column('id', db.Integer, primary_key=True, doc='id')
    user_id = db.Column(db.String, doc='用户id')
    group_id = db.Column(db.String, doc='用户组id')


class RoleGroup(db.Model):
    """
    角色-组表
    """
    __tablename__ = 'role_group'
    id = db.Column('id', db.Integer, primary_key=True, doc='id')
    role_id = db.Column(db.String, doc='角色id')
    group_id = db.Column(db.String, doc='用户组id')


class RolePermission(db.Model):
    """
    角色-组表
    """
    __tablename__ = 'role_permission'
    id = db.Column('id', db.Integer, primary_key=True, doc='id')
    role_id = db.Column(db.String, doc='角色id')
    permission_id = db.Column(db.String, doc='用户组id')


class MenuPermission(db.Model):
    """
    角色-组表
    """
    __tablename__ = 'menu_permission'
    id = db.Column('id', db.Integer, primary_key=True, doc='id')
    menu_id = db.Column(db.String, doc='菜单id')
    permission_id = db.Column(db.String, doc='权限id')


class Menu(db.Model):
    """
    角色-组表
    """
    __tablename__ = 'menu'
    id = db.Column('id', db.Integer, primary_key=True, doc='id')
    name = db.Column(db.String, doc='菜单')
    url = db.Column(db.String, doc='url地址')

