from flask_restful import Resource
from ticketing.common.modules.create_response import create_response

class Index(Resource):
    def get(self):
        return create_response('hello world')