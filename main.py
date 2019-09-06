from flask import Flask
import pymysql


# 配置文件对象
class DefaultConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/crm'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    JWT_SECRET = "deefefefefe"


app = Flask(__name__)

# 加载配置文件
app.config.from_object(DefaultConfig)


# 注册蓝图
from resource.crm import crm_bp
app.register_blueprint(crm_bp)

if __name__ == '__main__':
    app.run()

