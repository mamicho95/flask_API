#from my_app import app
from my_app.model.category import Category
from my_app.model.product import Product
from my_app import db,app





@app.route('/')
@app.route('/home')
@app.route('/home/<int:page>')
def index(page=1):
    #pageProducts = Product.query.paginate(page,5)   
    #return render_template('product/index.html',products=pageProducts)
    return "xd"