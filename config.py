import json

class ConfigError(Exception):
    pass

class Config:
    def __init__(self, filepath):
        self.filepath = filepath
        self.config_data = self.load_config()

    def load_config(self):
        try:
            with open(self.filepath, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise ConfigError(f"Configuration file '{self.filepath}' not found.")
        except json.JSONDecodeError:
            raise ConfigError(f"Failed to parse JSON from '{self.filepath}'.")
        except Exception as e:
            raise ConfigError(f"An unexpected error occurred: {str(e)}")

    def get_setting(self, key, default=None):
        if key not in self.config_data:
            return default
        return self.config_data[key]

# Example Usage
if __name__ == '__main__':
    try:
        config = Config('config.json')
        example_setting = config.get_setting('example_key', 'default_value')
        print(example_setting)
    except ConfigError as e:
        print(e)