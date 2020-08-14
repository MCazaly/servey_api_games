from .game import Game


class Dummy(Game):
    def __init__(self, game):
        super().__init__(game)

        self.info.online = "unknown"
        self.info.server_name = "Dummy McDumbface"
        self.info.game_name = "Dummy"
        self.info.player_count = "?"
        self.info.max_player_count = "?"
