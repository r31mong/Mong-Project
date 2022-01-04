import json

jsonob = json.load(open('sample.json'))
print(jsonob['people'][0]['firstName'])