from flask.views import MethodView
from flask import request
from my_app import app,db
from my_app.rest_api.helper.request import sendResJson
import json
#models
from my_app.model.category import Category

def categoryToJson(category: Category):
    return{
        'id': category.id,
        'name': category.name
            }

class CategoryAPI(MethodView):
    def get(self, id=None):
        if id:
            category = Category.query.get(id)
            res = categoryToJson(category)
            
        else:
            categories = Category.query.all()       
            res = []
            for c in categories:
                res.append(categoryToJson(c))
        return sendResJson(res,None,200)


category_view = CategoryAPI.as_view('category_view')
app.add_url_rule('/api/categories/',view_func=category_view, methods=['GET'])

app.add_url_rule('/api/categories/<int:id>/',view_func=category_view, methods=['GET'])