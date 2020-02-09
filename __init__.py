from flask import Flask
from flask_restplus import Resource, Api
import games


class Application(object):
    name = "ServeyMcServeface API"
    app = Flask(name)
    api = Api(app)
    api.title = name
    root = "/api/"

    def run(self):
        return self.app.run()

    def add_namespace(self, namespace):
        return self.api.add_namespace(namespace)


if __name__ == "__main__":
    flask_app = Application()
    flask_app.add_namespace(games.api)
    flask_app.run()
