from flask import Blueprint
from flask_restful import Api
from resources.Status import Status

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)

# Route
api.add_resource(Status, '/status')