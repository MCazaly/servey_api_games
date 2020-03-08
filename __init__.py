from flask import Flask
from flask_restplus import Api, Resource, Namespace
from . import games
from os import path
import json
from .games import Srcds
from .games import Minecraft

name = "ServeyMcServeface API (Games)"
app = Flask(name)
app.config["APPLICATION_ROOT"] = "/games/"

api = Api(app)

api.title = name

directory = path.dirname(path.abspath(__file__))
games_path = path.join(path.dirname(path.abspath(__file__)), "games.json")
if not path.isfile(games_path):
    with open(games_path, "w") as file:
        file.write("{}")
with open(games_path, "r") as file:
    games = json.load(file)

sources = {
    "srcds": Srcds,
    "minecraft": Minecraft
}


@api.route("/list")
class GameList(Resource):
    @staticmethod
    def get():
        return list(games.keys())


@api.route("/all")
class GameInfoAll(Resource):
    @staticmethod
    @api.doc("Get info for all games")
    def get():
        game_info = {}
        for game_id in games.keys():
            game = games[game_id]
            source = sources[game["source"]](game["address"])
            game_info[game_id] = source.get_dict()
        return game_info


@api.route("/game/<string:game_id>")
class GameInfo(Resource):
    @staticmethod
    @api.doc("Get game info")
    def get(game_id):
        game = games[game_id]
        source = sources[game["source"]](game["address"])
        return source.get_dict()


def main():
    app.run()


if __name__ == "__main__":
    main()
