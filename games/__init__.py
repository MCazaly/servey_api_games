import json
from flask_restplus import Namespace, Resource
from .srcds import Srcds
from .minecraft import Minecraft
from os import path


directory = path.dirname(path.abspath(__file__))
games_path = path.join(path.split(path.dirname(path.abspath(__file__)))[0], "games.json")
if not path.isfile(games_path):
    with open(games_path, "w") as file:
        file.write("{}")
with open(games_path, "r") as file:
    games = json.load(file)

sources = {
    "srcds": Srcds,
    "minecraft": Minecraft
}

api = Namespace("games", "Gameserver-related operations")


@api.route("/")
class GameList(Resource):
    @staticmethod
    def get():
        return list(games.keys())


@api.route("/game/<string:game_id>")
class GameInfo(Resource):
    @staticmethod
    @api.doc("Get game info")
    def get(game_id):
        game = games[game_id]
        source = sources[game["source"]](game["address"])
        return source.get_dict()
