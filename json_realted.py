import json
import os


def save_settings_json(data, filepath='config.json'):
    """Saves the given data to a JSON file, ensuring it exists."""
    try:
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error: Could not save settings to '{filepath}': {e}")


def load_settings_json(filepath='config.json'):
    """ Loads settings from a JSON file. """
    if not os.path.exists(filepath):
        print(f"Error: The file '{filepath}' was not found.")
        return None
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print(f"Error: The file '{filepath}' is not a valid JSON.")
        return None


def validate_json(filepath='config.json'):
    """ Validates the JSON file to ensure it contains the required keys. """
    if not os.path.exists(filepath):
        return False
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
        if not all(key in data for key in ("folders",
                                           "destination",
                                           "shuffle",
                                           "equals_amounts")):
            return False
    except json.JSONDecodeError:
        return False

    return True
