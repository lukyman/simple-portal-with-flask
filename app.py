from flask import  Flask, render_template, request, make_response,redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

Test = False
Dev = True
Prod = False
# dev database string
if Dev:
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://<db_username>:<password>@localhost/<database_name>?charset=utf8mb4&use_unicode=0"

# test database string
if Test:
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://<db_username>:<password>@localhost/<database_name>?charset=utf8mb4&use_unicode=0"

app.config['login_template'] = "/auth/login.html"
db = SQLAlchemy(app)

from controllers.dashboard import dashboard
from controllers.merchant import MerchantController
from controllers.float import FloatController
from controllers.portaluser import PortaluserController
from controllers.auth import AuthController

db.create_all()
migrate = Migrate(app,db)

if __name__ == '__main__':
    app.debug = True
    app.run()

