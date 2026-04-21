import json
from typing import Any, Dict

class RobloxDataHandler:
    @staticmethod
    def load_data(file_path: str) -> Dict[str, Any]:
        """Load JSON data from a file."""
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                return data
        except (FileNotFoundError, json.JSONDecodeError) as e:
            raise Exception(f'Error loading data: {str(e)}')

    @staticmethod
    def save_data(file_path: str, data: Dict[str, Any]) -> None:
        """Save data to a JSON file."""
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            raise Exception(f'Error saving data: {str(e)}')

    @staticmethod
    def update_data(file_path: str, updates: Dict[str, Any]) -> None:
        """Update existing JSON data in a file."""
        data = RobloxDataHandler.load_data(file_path)
        data.update(updates)
        RobloxDataHandler.save_data(file_path, data)

    @staticmethod
    def retrieve_value(data: Dict[str, Any], key: str) -> Any:
        """Retrieve a value from nested data safely."""
        keys = key.split('.');
        for k in keys:
            data = data.get(k, {})
        return data
