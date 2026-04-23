import json
import os

def read_json_file(file_path):
    """Reads a JSON file and returns the data."""
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    with open(file_path, 'r') as file:
        return json.load(file)


def write_json_file(file_path, data):
    """Writes data to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def get_env_variable(var_name):
    """Gets an environment variable, returns None if not found."""
    return os.getenv(var_name)


def safe_divide(numerator, denominator):
    """Performs safe division, returns None if denominator is zero."""
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return None


def format_roblock_id(game_id):
    """Formats the Roblox game ID for API requests."""
    return f"https://api.roblox.com/games/{game_id}"