
from flask import Flask

app = Flask(__name__)


# 注册蓝图
from resource.crm import crm_bp
app.register_blueprint(crm_bp)

if __name__ == '__main__':
    app.run()

