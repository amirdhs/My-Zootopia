import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')
output = ''
for item in animals_data:
    output += f"<li class='cards__item'>\n"
    output += f'<div class="{item["name"]}">{item["name"]}</div>\n'
    output += f'<p class="card__text">\n'
    output += f"<strong>Diet: </strong>{item['characteristics']['diet']}<br/>\n"
    output += f"<strong>Location: </strong>{item['locations'][0]}<br/>\n"
    if 'type' in item['characteristics']:
        output += f"<strong>Type: </strong>{item['characteristics']['type']}<br/>\n"
    output += f"</p>\n"
    output += f"</li>\n"

with open("animals_template.html", "r") as template_file:
    template_html = template_file.read()

updated_html = template_html.replace("__REPLACE_ANIMALS_INFO__", f"{output}")

with open("animals.html", "w") as output_file:
    output_file.write(updated_html)

print("HTML file updated successfully!")