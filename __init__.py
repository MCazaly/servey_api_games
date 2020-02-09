from flask import Flask
from flask_restplus import Api
from . import games

name = "ServeyMcServeface API"
app = Flask(name)
api = Api(app)
api.title = name
root = "/api/"

api.add_namespace(games.api)


def main():
    app.run()


if __name__ == "__main__":
    main()
