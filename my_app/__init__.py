from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config.from_object('configuration.DevelopmentConfig')


db = SQLAlchemy(app)
#rest 
from my_app.rest_api.product_api import product_view
from my_app.rest_api.category_api import category_view


#views
from my_app.rest_api.view import Product
db.create_all()