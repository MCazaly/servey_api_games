class Info(object):
    online = None
    server_name = None
    game_name = None
    map_name = None
    player_count = None
    max_player_count = None

    def __init__(self,
                 online: bool = False,
                 server_name: str = None,
                 game_name: str = None,
                 map_name: str = None,
                 player_count: int = None,
                 max_player_count: int = None):
        self.online = online
        self.server_name = server_name
        self.game_name = game_name
        self.map_name = map_name
        self.player_count = player_count
        self.max_player_count = max_player_count


class Game(object):
    info = None

    def __init__(self):
        self.info = Info()

    def get_info(self):
        return self.info

    def get_dict(self):
        return self.info.__dict__
