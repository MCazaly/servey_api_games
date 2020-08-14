from flask import Flask, url_for
from flask_restplus import Api, Resource
from . import games
from os import path
import json
from .games import A2s
from .games import Minecraft
from .games import LunaMultiplayer
from .games import Dummy
from .games import DayZ


name = "ServeyMcServeface API (Games)"
app = Flask(name)
app.config["APPLICATION_ROOT"] = "/games/"


class SecureApi(Api):
    @property
    def specs_url(self):
        # HTTPS monkey patch
        scheme = "http" if ":5000" in self.base_url else "https"
        return url_for(self.endpoint("specs"), _external=True, _scheme=scheme)


api = SecureApi(app, doc="/")

api.title = name

directory = path.dirname(path.abspath(__file__))
games_path = path.join(path.dirname(path.abspath(__file__)), "games.json")
if not path.isfile(games_path):
    with open(games_path, "w") as file:
        file.write("{}")
with open(games_path, "r") as file:
    games = json.load(file)

sources = {
    "a2s": A2s,
    "minecraft": Minecraft,
    "ksp_lmp": LunaMultiplayer,
    "dummy": Dummy,
    "dayz": DayZ
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

            source = sources[game["source"]](game)
            game_info[game_id] = source.get_dict()
        return game_info


@api.route("/game/<string:game_id>")
class GameInfo(Resource):
    @staticmethod
    @api.doc("Get game info")
    def get(game_id):
        game = games[game_id]
        source = sources[game["source"]](game)
        return source.get_dict()


def main():
    app.run()


if __name__ == "__main__":
    main()
