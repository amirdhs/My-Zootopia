import json

def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)

def serialize_animal(animal_obj):
    """Serializes an animal object into an HTML list item."""
    output = ''
    output += f"<li class='cards__item'>\n"
    output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'
    output += f'  <p class="card__text">\n'
    output += f"    <strong>Diet: </strong>{animal_obj['characteristics']['diet']}<br/>\n"
    output += f"    <strong>Location: </strong>{animal_obj['locations'][0]}<br/>\n"
    if 'type' in animal_obj['characteristics']:
        output += f"    <strong>Type: </strong>{animal_obj['characteristics']['type']}<br/>\n"
    output += f"  </p>\n"
    output += f"</li>\n"
    return output

def main():
    animals_data = load_data('animals_data.json')
    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)

    with open("animals_template.html", "r") as template_file:
        template_html = template_file.read()

    updated_html = template_html.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w") as output_file:
        output_file.write(updated_html)

    print("HTML file updated successfully!")



if __name__ == "__main__":
    main()