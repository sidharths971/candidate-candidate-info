from flask_restful import Resource
import logging as logger
import pandas as pd

class Task(Resource):

    def get(self):
        logger.debug('I am inside get method')
        return {'message': 'Hellow'}, 200
