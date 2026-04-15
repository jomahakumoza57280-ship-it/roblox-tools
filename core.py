import random
import json

class RobloxGame:
    def __init__(self, name, max_players):
        self.name = name
        self.max_players = max_players
        self.players = []

    def add_player(self, player_name):
        if len(self.players) < self.max_players:
            self.players.append(player_name)
        else:
            raise ValueError("Player limit reached.")

    def remove_player(self, player_name):
        try:
            self.players.remove(player_name)
        except ValueError:
            print(f"Player '{player_name}' not found.")

    def get_player_count(self):
        return len(self.players)

    def to_json(self):
        return json.dumps({
            'name': self.name,
            'max_players': self.max_players,
            'players': self.players
        })

    def __str__(self):
        return f"RobloxGame(name={self.name}, players={self.get_player_count()})"

if __name__ == '__main__':
    game = RobloxGame("Super fun game", 10)
    game.add_player("Player1")
    game.add_player("Player2")
    print(game)
    print(game.to_json())