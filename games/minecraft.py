from .game import Game
from socket import timeout as socket_timeout
import a2s


class Srcds(Game):
    def __init__(self, address):
        try:
            srcds_info = a2s.info(address)
        except socket_timeout:
            return
        self.info.online = True
        self.info.server_name = srcds_info.server_name
        self.info.game_name = srcds_info.game
        self.info.map_name = srcds_info.map_name
        self.info.player_count = srcds_info.player_count
        self.info.max_player_count = srcds_info.max_players
