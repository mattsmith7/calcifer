import json

with open("./data/exchange_content.json", "r") as file:
    data = json.load(file)

    for item in data:
        with open("./data/content/content-{0}.json".format(item["id"]), "w") as file:
            json.dump(item, file)

        file.close()

file.close()