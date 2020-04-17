class Info(object):
    online = None
    server_name = None
    game_name = None
    map_name = None
    player_count = None
    max_player_count = None
    title = None
    connect = None

    def __init__(self,
                 online: bool = False,
                 server_name: str = None,
                 game_name: str = None,
                 map_name: str = None,
                 player_count: int = None,
                 max_player_count: int = None,
                 title: str = None,
                 connect: str = None):
        self.online = online
        self.server_name = server_name
        self.game_name = game_name
        self.map_name = map_name
        self.player_count = player_count
        self.max_player_count = max_player_count
        self.title = title,
        self.connect = connect


class Game(object):
    info = None
    address = None

    def __init__(self, game):
        self.info = Info(title=game["title"], connect=game["connect"])
        self.address = game["address"]

    def get_info(self):
        return self.info

    def get_dict(self):
        return self.info.__dict__
