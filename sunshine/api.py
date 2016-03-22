
from flask import Blueprint

from flask_restful import Api, Resource

import pymysql

blueprint = Blueprint('api', __name__, url_prefix='/api', static_folder='../static')

api = Api(blueprint)

class Weather(Resource):

    def get(self, lat, lon):

        return dict(temp=72.0, pressure=1014.0)

api.add_resource(Weather, "/weather/<float:lat>/<float:lon>")
