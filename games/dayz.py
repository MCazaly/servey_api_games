from .dummy import Dummy


class DayZ(Dummy):
    def __init__(self, game):
        super().__init__(game)

        self.info.server_name = "DayZ"
        self.info.game_name = "DayZ"
