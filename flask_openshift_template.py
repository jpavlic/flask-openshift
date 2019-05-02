import os
from flask import Flask, render_template
from flask_restful import Api
from flask_jwt import JWT

from app.security import authenticate, identity
from app.resources.user import UserRegister
from app.resources.item import Item, ItemList
from app.resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:' + os.getenv("MYSQL_DB_PASSWORD") + '@' + os.getenv("MYSQL_DB_HOST") + '/falsk' #'sqlite:///flask.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)

@app.before_first_request
def create_tables():
    from app.db import db
    db.create_all()

# /auth
jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

# a simple page that says hello
@app.route("/")
def index():
    return render_template('index.html')


if __name__ == '__main__':
    from app.db import db
    db.init_app(app)
    app.run(debug=True)
