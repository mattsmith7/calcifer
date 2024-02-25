import pandas as pd
import json

#reads .csv file from data folder
data = pd.read_csv('./data/exchange-formatted-content.csv', header=0)
#converts .csv to json format
jsonData = data.to_dict(orient='records')
#opens new json file and dumps jsonData into it
with open("exchange_content.json", "w") as file:
    json.dump(jsonData, file)