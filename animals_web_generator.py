import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

for item in animals_data:
    print(f"name : {item['name']}")
    print(f"diet : {item['characteristics']['diet']}")
    print(f"Location : {item['locations'][0]}")
    if 'type' in item['characteristics']:
        print(f"Type : {item['characteristics']['type']}")
    print(30 * " ")





