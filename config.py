import json
import os

DEFAULT_CONFIG = {
    'username': 'guest',
    'avatar': 'default_avatar.png',
    'volume': 50,
    'language': 'en',
}

def load_config(file_path='config.json'):
    """Load configuration from a JSON file, merging with defaults."""
    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            try:
                user_config = json.load(f)
                # Merge user config with defaults
                config = {**DEFAULT_CONFIG, **user_config}
                return config
            except json.JSONDecodeError:
                print('Error decoding JSON, using defaults')
    return DEFAULT_CONFIG

if __name__ == '__main__':
    config = load_config()
    print(config)