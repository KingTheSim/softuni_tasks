from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player) -> str:
        if player.guild != "Unaffiliated":
            if self.name == player.guild:
                return f"Player {player.name} is already in the guild."

            else:
                return f"Player {player.name} is in another guild."

        else:
            player.guild = self.name
            self.players.append(player)
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str) -> str:
        for pl in self.players:
            if pl.name == player_name:
                self.players.remove(pl)
                pl.guild = "Unaffiliated"
                return f"Player {player_name} has been removed from the guild."

        else:
            return f"Player {player_name} is not in the guild."

    def guild_info(self) -> str:
        current_players = []
        for pl in self.players:
            current_players.append(pl.player_info())
        current_players = "\n".join(current_players)
        return f"Guild: {self.name}\n" \
               f"{current_players}"


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())

guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
