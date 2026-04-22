from typing import List, Dict, Any

class DataProcessor:
    """Class to process Roblox game data."""

    def __init__(self, game_data: List[Dict[str, Any]]) -> None:
        """Initialize processor with game data.

        Args:
            game_data (List[Dict[str, Any]]): A list of game data dictionaries.
        """
        self.game_data = game_data

    def filter_by_attribute(self, attribute: str, value: Any) -> List[Dict[str, Any]]:
        """Filter game data by a specified attribute.

        Args:
            attribute (str): The key to filter by.
            value (Any): The value that the key should match.

        Returns:
            List[Dict[str, Any]]: Filtered list of game data.
        """
        return [entry for entry in self.game_data if entry.get(attribute) == value]

    def summarize_data(self) -> Dict[str, int]:
        """Summarize the game data.

        Returns:
            Dict[str, int]: A dictionary with the count of entries by category.
        """
        summary = {}
        for entry in self.game_data:
            category = entry.get('category', 'Unknown')
            summary[category] = summary.get(category, 0) + 1
        return summary

    def extract_names(self) -> List[str]:
        """Extract names from game data.

        Returns:
            List[str]: A list of names.
        """
        return [entry['name'] for entry in self.game_data if 'name' in entry]