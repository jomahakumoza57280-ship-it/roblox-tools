import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Game:
    def __init__(self, title):
        self.title = title
        self.players = []

    def add_player(self, player):
        if player not in self.players:
            self.players.append(player)
            logger.info(f'{player} joined {self.title}.')
        else:
            logger.warning(f'{player} is already in the game.')

    def remove_player(self, player):
        if player in self.players:
            self.players.remove(player)
            logger.info(f'{player} left {self.title}.')
        else:
            logger.warning(f'{player} is not in the game.')

    def list_players(self):
        return self.players

if __name__ == '__main__':
    game = Game('Roblox Fun')
    game.add_player('Alice')
    game.add_player('Bob')
    game.remove_player('Alice')
    logger.info(f'Current players: {game.list_players()}')