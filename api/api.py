import os
from flask import Flask, send_from_directory
from flask_restful import Api
from resources import *
from security import identity, authenticate
from flask_jwt import JWT

# ============================================================================================
# =================================================================== INITIALIZATION =========
# ============================================================================================

# Create a new Flask application
app = Flask(__name__)
# Add a secret key. Important for hashing (e.g. with login handling)
app.secret_key = os.getenv('SECRET')
# Create a new API
api = Api(app, prefix=os.getenv('API_PREFIX'))
app.config['JWT_AUTH_URL_RULE'] = os.getenv('API_PREFIX') + '/auth'
jwt = JWT(app, authenticate, identity)

# ============================================================================================
# =============================================================== FRONTEND REDIRECTS =========
# ============================================================================================

@app.route('/')
def index():
    """Redirects the base url '/' to the webshop/index.html file

    Returns:
        string: file content
    """
    return send_from_directory('../webshop', 'index.html')

@app.route('/<path:path>')
def shop(path):
    """Redirects all requests to the front end (webshop)

    Args:
        path (path): path to requested file

    Returns:
        string: file content
    """
    return send_from_directory('../webshop', path)
    
# ============================================================================================
# =================================================================== ERROR HANDLING =========
# ============================================================================================

@app.errorhandler(404)
def page_not_found(e):
    """Returns a JSON on 404
    
    Returns:
        object: error message
    """
    return {'message': 'resource not found'}, 404
    
# ============================================================================================
# ======================================================================== ENDPOINTS =========
# ============================================================================================

api.add_resource(Categories, '/categories')
api.add_resource(Products, '/categories/<int:id>/products')
api.add_resource(Product, '/products/<int:id>')
api.add_resource(Countries, '/countries')
api.add_resource(FindProduct, '/products', endpoint="q")
api.add_resource(RegisterUser, '/users')
api.add_resource(loginNaam, '/users/me')
# shows Userrolles if admin => login as admin
api.add_resource(Userroles, '/userroles')
api.add_resource(PlaceOrder, '/orders')
api.add_resource(GetOrder, '/users/<int:id>/orders')
api.add_resource(GetOrders, '/orders')
api.add_resource(EditProduct, '/products/<int:id>')
api.add_resource(AddCategory, '/categories')
api.add_resource(AddCountry, '/countries')
api.add_resource(RemoveProduct, '/products/<int:id>')
api.add_resource(ChangeOrderStatus, '/orders/<int:id>')
api.add_resource(EditUser, '/users/<int:id>')

# ================================================D============================================
# ================================================================ START APPLICATION =========
# ============================================================================================

if __name__ == '__main__':
    app.run(debug=True)
