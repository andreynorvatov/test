import yaml
from yaml.loader import SafeLoader


def compare_dicts(dict1, dict2):
    for key in dict1:
        if key in dict2:
            #if type(dict1[key]) is dict:
            if isinstance(dict1[key], dict):
                compare_dicts(dict1[key], dict2[key])
            elif dict1[key] != dict2[key]:
                print(f"Value mismatch for key '{key}': {dict1[key]} != {dict2[key]}")
        else:
            print(f"Key '{key}' not found in second dictionary")
    for key in dict2:
        if key not in dict1:
            print(f"Key '{key}' with value '{dict2[key]}' not found in first dictionary")

with open('docker-compose.yml') as f:
    data1 = yaml.load(f, Loader=SafeLoader)
    print(data1)

with open('docker-compose2.yml') as f:
    data2 = yaml.load(f, Loader=SafeLoader)
    print(data2)

compare_dicts(data1, data2)