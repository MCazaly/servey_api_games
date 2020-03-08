from flask import Flask, Blueprint
from flask_restplus import Api
from . import games

name = "ServeyMcServeface API"
app = Flask(name)
app.config["SERVER_NAME"] = "api.serveymcserveface.com:80"
app.config["APPLICATION_ROOT"] = "/games"
api = Api(app)
api.title = name

api.add_namespace(games.api)


def main():
    app.run()


if __name__ == "__main__":
    main()
