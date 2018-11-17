import json

def return_json():
    l = []
    l.append(1)
    l.append(2)
    l.append(3)

    return json.dumps(l)
