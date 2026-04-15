import json
import os

def load_json_file(file_path):
    """Load a JSON file and return its contents as a dictionary."""
    try:
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {file_path}")
    except Exception as e:
        raise RuntimeError(f"An error occurred: {str(e)}")


def save_json_file(file_path, data):
    """Save a dictionary to a JSON file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError:
        raise RuntimeError(f"Unable to write to file: {file_path}")
    except Exception as e:
        raise RuntimeError(f"An error occurred: {str(e)}")


def validate_data_structure(data, expected_keys):
    """Check the data structure for required keys."""
    missing_keys = [key for key in expected_keys if key not in data]
    if missing_keys:
        raise KeyError(f'Missing keys in data: {missing_keys}')