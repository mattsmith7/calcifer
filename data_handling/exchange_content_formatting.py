import json


with open("./data/exchange_content.json", "r") as file:
    data = json.load(file)

    for item in data:

        newItem = item["tags"][0].replace("}]", "")

        item["tags"][0] = newItem

        print(item["tags"][0])

    
with open("./data/exchange_content.json", "w") as file:
    json.dump(data, file)

file.close()