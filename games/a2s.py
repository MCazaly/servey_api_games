from .game import Game
from socket import timeout as socket_timeout
import a2s


class A2s(Game):
    def __init__(self, game):
        super().__init__(game)
        try:
            a2s_info = a2s.info(tuple(self.address))
        except (socket_timeout, a2s.BrokenMessageError):
            return
        self.info.online = True
        self.info.server_name = a2s_info.server_name
        self.info.game_name = a2s_info.game
        self.info.map_name = a2s_info.map_name
        self.info.player_count = a2s_info.player_count
        self.info.max_player_count = a2s_info.max_players
        self.info.a2s = {
            "folder": a2s_info.folder,
            "app_id": a2s_info.app_id,
            "bot_count": a2s_info.bot_count,
            "password_protected": a2s_info.password_protected,
            "vac_enabled": a2s_info.vac_enabled,
            "version": a2s_info.version,
        }
