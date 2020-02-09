from flask_restplus import Resource

class Srcds(Resource):
    api = None

    def __init__(self, api):
        super().__init__()
        self.api = api
