import json

def save_entities_to_json(entities, filename):
    try:
        with open(filename, 'w') as json_file:
            json.dump(entities, json_file, indent=4)
        print(f"Entities saved to {filename}")
    except IOError as e:
        print(f"Error saving the file: {e}")
