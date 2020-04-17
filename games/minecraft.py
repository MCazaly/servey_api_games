from .game import Game
import mcstatus


class Minecraft(Game):
    def __init__(self, game):
        super().__init__(game)
        try:
            server = mcstatus.MinecraftServer(self.address[0], port=self.address[1])
            minecraft_info = server.status()
        except ConnectionError:
            return
        self.info.online = True
        self.info.server_name = minecraft_info.description["text"]
        self.info.game_name = f"Minecraft {minecraft_info.version.name}"
        self.info.player_count = minecraft_info.players.online
        self.info.max_player_count = minecraft_info.players.max
        self.info.minecraft = {
            "mods": minecraft_info.raw["modinfo"]["modList"]
        }
