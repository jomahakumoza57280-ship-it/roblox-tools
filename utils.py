import json

def load_json(file_path):
    """Load JSON data from a file."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f'Error loading JSON: {e}')
        return None


def save_json(data, file_path):
    """Save data to a JSON file."""
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f'Error saving JSON: {e}')


def generate_unique_id(existing_ids):
    """Generate a unique ID not in the existing IDs set."""
    new_id = 1
    while new_id in existing_ids:
        new_id += 1
    return new_id


def format_player_name(player_name):
    """Format a player name to title case."""
    return player_name.strip().title()


def is_valid_username(username):
    """Check if a username is valid (between 3 and 20 chars)."""
    return 3 <= len(username) <= 20
