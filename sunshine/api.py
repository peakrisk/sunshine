
from flask import Blueprint

from flask_restful import Api, Resource

from sunshine.settings import ProdConfig

import pymysql

import json

blueprint = Blueprint('api', __name__, url_prefix='/api', static_folder='../static')

api = Api(blueprint)


class Weather(Resource):
    

    def get(self, lat, lon):

        creds = credentials()
        
        connection = pymysql.connect(user=creds['user'], password=creds['password'],
                                     database=ProdConfig.WEATHER_DB)

        cursor = connection.cursor()

        cursor.execute("SELECT * from maxtemp where lat=%f and lon=%f and year=2015")

        result = cursor.fetchall()

        names = [x[0] for x in c.description]
        data = []
        for row in result:
            record = dict(zip(names, row))
            data.append(record)
        
        return record

class Tester(Resource):
    

    def get(self):

        return dict(a=1, b=1)

    
def credentials():

    with open(ProdConfig.CREDENTIALS) as infile:
        creds = json.loads(infile.read())

    return creds
        
api.add_resource(Weather, "/weather/<float:lat>/<float:lon>")
api.add_resource(Tester, "/tester")


