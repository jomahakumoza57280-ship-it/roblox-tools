import json
import logging

# Configure logging
def configure_logging(log_file='app.log'):
    logging.basicConfig(
        filename=log_file,
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

# Load JSON from a file with error handling
def load_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error(f'File not found: {file_path}')
        return None
    except json.JSONDecodeError:
        logging.error(f'Error decoding JSON from file: {file_path}')
        return None
    except Exception as e:
        logging.error(f'Unexpected error occurred: {str(e)}')
        return None

# Save JSON to a file with error handling
def save_json_to_file(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError:
        logging.error(f'Error writing to file: {file_path}')
    except Exception as e:
        logging.error(f'Unexpected error occurred: {str(e)}')
