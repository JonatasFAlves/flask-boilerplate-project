from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)

# Route
api.add_resource(Hello, '/hello')