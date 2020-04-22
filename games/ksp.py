from .game import Game
import requests


class LunaMultiplayer(Game):
    def __init__(self, game):
        super().__init__(game)
        host, port = game["address"]
        try:
            response = requests.get(f"http://{host}:{port}")
            response.raise_for_status()
        except (requests.HTTPError, UnicodeDecodeError, requests.exceptions.ConnectionError):
            return
        ksp_info = response.json()[0]
        self.info.online = True
        self.info.server_name = ksp_info["GeneralSettings"]["ServerName"]
        self.info.game_name = "Kerbal Space Program"
        self.info.player_count = len(ksp_info["CurrentState"]["CurrentPlayers"])
        self.info.max_player_count = ksp_info["GeneralSettings"]["MaxPlayers"]
        self.info.ksp = ksp_info
