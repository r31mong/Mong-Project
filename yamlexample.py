import yaml
from yaml import load, load_all

stream = open('sample.yaml','r')
documents = load_all(stream, Loader=yaml.FullLoader)

print(type(documents))