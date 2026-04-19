from typing import List, Dict, Any

class RobloxPlayer:
    def __init__(self, username: str, age: int, is_online: bool) -> None:
        """Initialize a RobloxPlayer instance."""
        self.username: str = username
        self.age: int = age
        self.is_online: bool = is_online

    def get_player_info(self) -> Dict[str, Any]:
        """Return the player's info as a dictionary."""
        return {
            'username': self.username,
            'age': self.age,
            'is_online': self.is_online
        }

def filter_online_players(players: List[RobloxPlayer]) -> List[RobloxPlayer]:
    """Filter out online players from the list."""
    return [player for player in players if player.is_online]

def find_player_by_username(players: List[RobloxPlayer], username: str) -> RobloxPlayer:
    """Find a player by their username."""
    for player in players:
        if player.username == username:
            return player
    raise ValueError(f'Player with username {username} not found.')