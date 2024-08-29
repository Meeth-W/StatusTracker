import yaml
import json

class ConfigManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.config_data = None
        self._load_config()

    def _load_config(self):
        """Load the YAML configuration file."""
        with open(self.file_path, 'r') as file:
            self.config_data = yaml.safe_load(file)

    def save_config(self):
        """Save the current configuration data to the YAML file."""
        with open(self.file_path, 'w') as file:
            yaml.safe_dump(self.config_data, file)

    def fetch(self, key, default=None):
        """Get a value from the configuration data."""
        return self.config_data.get(key, default)

    def push(self, key, value):
        """Set a value in the configuration data."""
        self.config_data[key] = value
        self.save_config()

    def purge(self, key):
        """Delete a key from the configuration data."""
        if key in self.config_data:
            del self.config_data[key]
            self.save_config()

    def get_json(self):
        """Convert the configuration data to a JSON string."""
        return json.dumps(self.config_data, indent=4)