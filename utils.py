import json
import os

# Utility function for loading Roblox data from a JSON file

def load_roblox_data(file_path):
    """
    Loads Roblox data from a given JSON file.
    Raises FileNotFoundError if the file does not exist.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in file: {file_path}")

# Utility function for saving Roblox data to a JSON file

def save_roblox_data(file_path, data):
    """
    Saves the provided data as JSON to a file.
    Raises ValueError if data is not serializable.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except TypeError:
        raise ValueError("Provided data is not serializable to JSON.")

# Example usage:
if __name__ == '__main__':
    example_data = {'name': 'Roblox Game', 'players': 100}
    save_roblox_data('game_data.json', example_data)
    loaded_data = load_roblox_data('game_data.json')
    print(loaded_data)