from flask.views import MethodView
from flask import request
from my_app import app,db
from my_app.rest_api.helper.request import sendResJson
import json
#models
from my_app.model.product import Product

def productToJson(product: Product):
    return{
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'category_id': product.category_id,
        'category_name': product.category.name

    }

class ProductAPI(MethodView):
    def get(self, id=None):
        if id:
            products = Product.query.get(id)
            res = productToJson(products)
            
        else:
            products = Product.query.all()       
            res = []
            for p in products:
                res.append(productToJson(p))
        return sendResJson(res,None,200)

    def delete(self,id):
        try:
            product_id = int(id)
        except ValueError:
            return sendResJson(None,"parametro 'product_id' tipo de dato no valido",403)

        validateProduct = Product.query.filter_by(id = product_id).first()
        if not validateProduct:
            return sendResJson(None,f"No se encuentra este producto con id '{product_id}' ",403)

        p = Product.query.get(product_id)   
        db.session.delete(p)
        db.session.commit()
        return sendResJson(None,"producto eliminado",200)                    

    def post(self):
        if not request.form:
            return sendResJson(None,"Sin parametros",403)

        #validacion nombre
        
        if not "name" in request.form:
            return sendResJson(None,"Sin parametro 'name' ",403)
        name = request.form["name"]
        if len(name) < 3:
            return sendResJson(None,"parametro 'name' invalido, debe contener mas de 3 caracteres",403)

        

        #validacion precio
        if not "price" in request.form:
            return sendResJson(None,"Sin parametro 'price' ",403)   

        try:
           price = float(request.form["price"])
        except ValueError:
            return sendResJson(None,"parametro 'price' tipo de dato no valido",403)        

        #validacion categoria
        if not "category_id" in request.form:
            return sendResJson(None,"Sin parametro 'category_id' ",403)

        try:
           category_id = int(request.form["category_id"])
        except ValueError:
            return sendResJson(None,"parametro 'category_id' tipo de dato no valido",403)  

        validateUser = Product.query.filter_by(category_id = category_id).first()
        if not validateUser:
            return sendResJson(None,"parametro 'category_id' categoria no registrada",403)

        p = Product(name,price,category_id)
        db.session.add(p)
        db.session.commit()

        return sendResJson(productToJson(p),None,200)    

    def put(self,id):
        if not request.form:
            return sendResJson(None,"Sin parametros",403)

        product = Product.query.get(id)
        print('---------------')
        print(product)

        if not product:
            return sendResJson(None,"No existe este producto",403)
        #validacion nombre
        if not "name" in request.form:
            #name = product.name
            pass
        else:
            product.name = request.form["name"]
        if len(product.name) < 3:
            return sendResJson(None,"parametro 'name' invalido, debe contener mas de 3 caracteres",403)

        

        #validacion precio
        if not "price" in request.form:
            #price = product.price   
            pass
        else:            
            try:
                product.price = float(request.form["price"])
            except ValueError:
                return sendResJson(None,"parametro 'price' tipo de dato no valido",403)        

        #validacion categoria
        if not "category_id" in request.form:
            #category_id = product.category_id
            pass
        else:
            try:
                product.category_id = int(request.form["category_id"])
                validateCategory = Product.query.filter_by(category_id = product.category_id).first()
                if not validateCategory:
                    return sendResJson(None,"parametro 'category_id' categoria no registrada",403)             
            except ValueError:
                return sendResJson(None,"parametro 'category_id' tipo de dato no valido",403)  

        #p = Product(name,price,category_id)
        db.session.add(product)
        db.session.commit()

        return sendResJson(None,"Producto actualizado con exito ",200)    

product_view = ProductAPI.as_view('product_view')
app.add_url_rule('/api/products/',view_func=product_view, methods=['GET','POST'])

app.add_url_rule('/api/products/<int:id>/',view_func=product_view, methods=['GET','DELETE','PUT'])