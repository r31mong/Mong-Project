import yaml
from yaml import load, load_all

stream = open('sample4.yaml','r')
data = load_all(stream, Loader=yaml.FullLoader)

for doc in data:
        print("New Document:")
        for key, value in doc.items():
                print(key + ": " + str(value))
                if type(value) is list:
                        print(str(len(value)))
                        