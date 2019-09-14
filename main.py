from flask import Flask
import pymysql


# 配置文件对象
class DefaultConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/crm'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    JWT_SECRET = "testcrm"
    HOSTS = "http://127.0.0.1:5000"  # 配置运行环境ip


app = Flask(__name__)


# 获取请求钩子
from common.utils.middlewares import jwt_authentication
app.before_request(jwt_authentication)

# 加载配置文件
app.config.from_object(DefaultConfig)


# 注册蓝图
from resource.crm import crm_bp
app.register_blueprint(crm_bp)

if __name__ == '__main__':
    app.run()

