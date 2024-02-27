import json


with open("./data/exchange_content.json", "r") as file:
    data = json.load(file)

    for item in data:
        if item['prices'] is None:
            
            item['prices'] = []


with open("./data/exchange_content.json", "w") as file:
    json.dump(data, file)

file.close()