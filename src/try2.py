import json 

with open('artilces.json', 'r') as file: 
    data = json.load(file)


print(len(data))