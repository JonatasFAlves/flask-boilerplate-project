from flask_restful import Resource

class Hello(Resource):
    def get():
        return "Hello World"