
from flask import Blueprint

from flask_restful import Api, Resource

from sunshine.settings import ProdConfig

import pymysql

import json

blueprint = Blueprint('api', __name__, url_prefix='/api', static_folder='../static')

api = Api(blueprint)


class Weather(Resource):
    

    def get(self, field, lat=72.0, lon=36.0):

        try:
            creds = credentials()
        except:
            return dict(cred='failed')
        
        connection = pymysql.connect(user=creds['user'], password=creds['password'],
                                     database=ProdConfig.WEATHER_DB)

        cursor = connection.cursor()


        sql = "SELECT * from %s where lat=%f and lon=%f"

        sql = sql % (field, lat, lon)

        cursor.execute(sql)

        result = cursor.fetchall()

        names = [x[0] for x in cursor.description]
        data = []
        for row in result:
            record = dict(zip(names, row))
            data.append(record)
        
        return data

class Tester(Resource):
    

    def get(self, choice):

        if choice == 1:
            return dict(z=20, w=90)
        
        return dict(a=1, b=1)

    
def credentials():

    with open(ProdConfig.CREDENTIALS) as infile:
        creds = json.loads(infile.read())

    return creds
        
api.add_resource(Weather, "/weather/<field>/<float:lat>/<float:lon>")
api.add_resource(Tester, "/tester/<int:choice>")


