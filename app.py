from flask import Flask
from base.controller import controller


app = Flask(__name__)

# 配置数据库连接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@39.106.180.44:3306/vsk'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True



controller(app)



@app.route('/')
def hello_world():



    return 'Hello World!'


if __name__ == '__main__':
    app.run()
