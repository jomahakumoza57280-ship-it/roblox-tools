import json
from typing import Any, Dict, List

class RobloxDataHandler:
    def __init__(self, data: Dict[str, Any]) -> None:
        self.data = data

    def get_value(self, key: str) -> Any:
        """Retrieve value by key from data."""
        return self.data.get(key, None)

    def update_value(self, key: str, value: Any) -> None:
        """Update the value for a given key."""
        self.data[key] = value

    def to_json(self) -> str:
        """Convert data to JSON string."""
        return json.dumps(self.data)

    def from_json(self, json_data: str) -> None:
        """Load data from a JSON string."""
        self.data = json.loads(json_data)

    def get_all_keys(self) -> List[str]:
        """Return a list of all keys in data."""
        return list(self.data.keys())

    def get_filtered_data(self, filter_func) -> Dict[str, Any]:
        """Return filtered data based on a filter function."""
        return {key: value for key, value in self.data.items() if filter_func(key, value)}

# Example of usage:
# handler = RobloxDataHandler({'player1': 100, 'player2': 200})
# handler.update_value('player1', 150)
# print(handler.to_json())
