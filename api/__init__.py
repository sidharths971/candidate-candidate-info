from flask_restful import Api
from app import app
from .task import Task

restserver = Api(app)
restserver.add_resource(Task, '/get/data/')
