from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired
from my_app import db
class Category(db.Model):    
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    products = db.relationship('Product', backref='category', lazy='select')
    
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<Category {self.name!r}>'    

class CategoryForm(FlaskForm):
    name = StringField('Nombre',validators=[InputRequired()])        